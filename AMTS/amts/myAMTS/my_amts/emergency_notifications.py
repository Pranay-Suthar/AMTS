# my_amts/emergency_notifications.py

import random
from django.core.mail import send_mail, send_mass_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Bus, ActiveBus, Booking
from datetime import datetime, date
import logging

logger = logging.getLogger(__name__)

class EmergencyNotificationSystem:
    """
    Emergency Accident Notification System for AMTS
    Handles email notifications to passengers and emergency contacts
    """
    
    def __init__(self):
        self.emergency_helplines = getattr(settings, 'EMERGENCY_HELPLINES', [
            'emergency@amts.gov.in',
            'control.room@amts.gov.in',
            'safety@amts.gov.in',
            'admin@amts.gov.in'
        ])
    
    def get_random_users(self, count=40):
        """
        Select random users from database for emergency notification
        Returns users with email addresses
        """
        try:
            # Get all users with email addresses
            users_with_emails = User.objects.filter(
                email__isnull=False,
                email__gt='',
                is_active=True
            ).exclude(is_staff=True)  # Exclude staff members
            
            total_users = users_with_emails.count()
            
            if total_users == 0:
                logger.warning("No users with email addresses found")
                return []
            
            # If we have fewer users than requested, return all
            if total_users <= count:
                return list(users_with_emails)
            
            # Get random users
            random_users = random.sample(list(users_with_emails), count)
            return random_users
            
        except Exception as e:
            logger.error(f"Error selecting random users: {str(e)}")
            return []
    
    def get_affected_passengers(self, bus_number):
        """
        Get passengers who have bookings for the affected bus today
        """
        try:
            today = date.today()
            affected_bookings = Booking.objects.filter(
                bus_number=bus_number,
                booking_date__date=today
            ).select_related('user')
            
            passengers = []
            for booking in affected_bookings:
                if booking.user.email:  # Only include users with email
                    passengers.append({
                        'user': booking.user,
                        'booking': booking
                    })
            
            return passengers
            
        except Exception as e:
            logger.error(f"Error getting affected passengers: {str(e)}")
            return []
    
    def generate_google_maps_link(self, latitude, longitude):
        """
        Generate Google Maps link from GPS coordinates
        """
        if latitude and longitude:
            return f"https://www.google.com/maps?q={latitude},{longitude}"
        return "Location unavailable"
    
    def get_route_name(self, bus_number):
        """
        Get route name for the bus
        """
        try:
            bus = Bus.objects.get(bus_number=bus_number)
            stops = bus.stops
            if stops and len(stops) >= 2:
                return f"{stops[0]['name']} ↔ {stops[-1]['name']}"
            return f"Route {bus_number}"
        except Bus.DoesNotExist:
            return f"Route {bus_number}"
    
    def send_emergency_emails(self, bus_number, latitude, longitude, accident_location=None):
        """
        Main function to send emergency emails for bus accident
        """
        try:
            # Get bus and route information
            route_name = self.get_route_name(bus_number)
            maps_link = self.generate_google_maps_link(latitude, longitude)
            
            # Location string
            if accident_location:
                location_str = f"{accident_location} ({maps_link})"
            else:
                location_str = f"GPS: {latitude}, {longitude} ({maps_link})"
            
            # Get affected passengers (actual bookings)
            affected_passengers = self.get_affected_passengers(bus_number)
            
            # Get random users for emergency notification (simulate family members)
            random_users = self.get_random_users(40)
            
            # Prepare email data
            timestamp = datetime.now().strftime('%d/%m/%Y at %I:%M %p')
            
            # Email content for affected passengers
            passenger_subject = f"🚨 URGENT: Bus Accident Alert - Bus {bus_number}"
            passenger_message = f"""EMERGENCY NOTIFICATION - AMTS

🚨 ACCIDENT ALERT 🚨

An accident involving Bus {bus_number} has been reported.

📍 Location: {location_str}
🚌 Bus Number: {bus_number}
🛣️ Route: {route_name}
⏰ Time: {timestamp}

If you or your family member was traveling on this bus, please:
1. Contact emergency services: 108
2. Call AMTS Control Room: +91-79-2658-0000
3. Visit the accident location if safe to do so

AMTS is coordinating with emergency services for immediate assistance.

Stay safe,
AMTS Emergency Response Team"""

            # Email content for random users (family emergency)
            family_subject = f"🚨 FAMILY EMERGENCY: Possible Bus Accident - Bus {bus_number}"
            family_message = f"""EMERGENCY NOTIFICATION - AMTS

🚨 FAMILY EMERGENCY ALERT 🚨

An accident involving your family member has occurred.

📍 Location: {location_str}
🚌 Bus Number: {bus_number}
🛣️ Route: {route_name}
⏰ Time: {timestamp}

Please contact emergency services or the AMTS control room immediately:
- Emergency Services: 108
- AMTS Control Room: +91-79-2658-0000
- Police: 100
- Fire: 101

Location on Google Maps: {maps_link}

AMTS Emergency Response Team is on-site providing assistance.

Immediate Action Required,
AMTS Emergency Response Team"""

            # Email content for emergency helplines
            helpline_subject = f"🚨 BUS ACCIDENT REPORT - Bus {bus_number} - Immediate Response Required"
            helpline_message = f"""EMERGENCY INCIDENT REPORT - AMTS

🚨 BUS ACCIDENT DETECTED 🚨

INCIDENT DETAILS:
- Bus Number: {bus_number}
- Route: {route_name}
- Location: {location_str}
- GPS Coordinates: {latitude}, {longitude}
- Time: {timestamp}

AFFECTED PASSENGERS: {len(affected_passengers)} confirmed bookings
EMERGENCY NOTIFICATIONS SENT: {len(random_users)} family alerts

IMMEDIATE ACTIONS REQUIRED:
1. Dispatch emergency response team
2. Coordinate with local emergency services
3. Set up family assistance center
4. Prepare medical support
5. Notify media relations team

Google Maps Location: {maps_link}

This is an automated emergency alert from AMTS Safety System.
Please respond immediately.

AMTS Emergency Response System"""

            # Send emails
            emails_sent = 0
            failed_emails = []
            
            # 1. Send to affected passengers
            for passenger_data in affected_passengers:
                try:
                    send_mail(
                        passenger_subject,
                        passenger_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [passenger_data['user'].email],
                        fail_silently=False,
                    )
                    emails_sent += 1
                    logger.info(f"Emergency email sent to passenger: {passenger_data['user'].email}")
                except Exception as e:
                    failed_emails.append(passenger_data['user'].email)
                    logger.error(f"Failed to send email to passenger {passenger_data['user'].email}: {str(e)}")
            
            # 2. Send to random users (family emergency)
            for user in random_users:
                try:
                    send_mail(
                        family_subject,
                        family_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [user.email],
                        fail_silently=False,
                    )
                    emails_sent += 1
                    logger.info(f"Family emergency email sent to: {user.email}")
                except Exception as e:
                    failed_emails.append(user.email)
                    logger.error(f"Failed to send family emergency email to {user.email}: {str(e)}")
            
            # 3. Send to emergency helplines
            for helpline_email in self.emergency_helplines:
                try:
                    send_mail(
                        helpline_subject,
                        helpline_message,
                        settings.DEFAULT_FROM_EMAIL,
                        [helpline_email],
                        fail_silently=False,
                    )
                    emails_sent += 1
                    logger.info(f"Emergency alert sent to helpline: {helpline_email}")
                except Exception as e:
                    failed_emails.append(helpline_email)
                    logger.error(f"Failed to send email to helpline {helpline_email}: {str(e)}")
            
            # Log emergency notification
            self.log_emergency_notification(
                bus_number, latitude, longitude, 
                len(affected_passengers), len(random_users), 
                emails_sent, failed_emails
            )
            
            return {
                'status': 'success',
                'emails_sent': emails_sent,
                'affected_passengers': len(affected_passengers),
                'family_alerts': len(random_users),
                'helpline_alerts': len(self.emergency_helplines),
                'failed_emails': failed_emails,
                'accident_details': {
                    'bus_number': bus_number,
                    'route': route_name,
                    'location': location_str,
                    'maps_link': maps_link,
                    'timestamp': timestamp
                }
            }
            
        except Exception as e:
            logger.error(f"Error in emergency notification system: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }
    
    def log_emergency_notification(self, bus_number, latitude, longitude, 
                                 affected_count, family_count, emails_sent, failed_emails):
        """
        Log emergency notification details for audit trail
        """
        try:
            log_message = f"""
EMERGENCY NOTIFICATION LOG
========================
Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Bus Number: {bus_number}
GPS Location: {latitude}, {longitude}
Affected Passengers: {affected_count}
Family Alerts Sent: {family_count}
Total Emails Sent: {emails_sent}
Failed Emails: {len(failed_emails)}
Failed Recipients: {', '.join(failed_emails) if failed_emails else 'None'}
========================
"""
            logger.critical(log_message)
            
            # Also write to a separate emergency log file
            import os
            log_dir = os.path.join(settings.BASE_DIR, 'logs')
            os.makedirs(log_dir, exist_ok=True)
            
            log_file = os.path.join(log_dir, 'emergency_notifications.log')
            with open(log_file, 'a', encoding='utf-8') as f:
                f.write(log_message + '\n')
                
        except Exception as e:
            logger.error(f"Error logging emergency notification: {str(e)}")

    def send_sms_notifications(self, phone_numbers, message):
        """
        SMS notification system (placeholder for future implementation)
        Currently logs to console for localhost testing
        """
        try:
            logger.info("SMS NOTIFICATIONS (Console Mode)")
            logger.info("=" * 50)
            
            for phone in phone_numbers:
                logger.info(f"SMS to {phone}: {message}")
            
            logger.info("=" * 50)
            
            return {
                'status': 'success',
                'sms_sent': len(phone_numbers),
                'mode': 'console_logging'
            }
            
        except Exception as e:
            logger.error(f"Error in SMS notification: {str(e)}")
            return {
                'status': 'error',
                'message': str(e)
            }