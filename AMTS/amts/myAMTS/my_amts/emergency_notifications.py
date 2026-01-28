# my_amts/emergency_notifications.py

import random
import time
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
            'vaibhavmevada796@gmail.com',  # Primary Emergency Contact
            'cipaha2099@gxuzi.com',  # Test Email for Emergency Notifications
            'emergency@amts.gov.in',
            'control.room@amts.gov.in',
            'safety@amts.gov.in',
            'admin@amts.gov.in'
        ])
    
    def get_priority_users_for_emergency(self, max_users=0):
        """
        Get priority users for emergency notification
        For now, only send to emergency helplines from settings.py to avoid rate limiting
        """
        try:
            # For now, return empty list to only use emergency helplines from settings
            # This avoids Gmail rate limiting and focuses on the important emails
            logger.info("Using only emergency helplines from settings.py for notifications")
            return []
            
        except Exception as e:
            logger.error(f"Error getting priority users for emergency: {str(e)}")
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
            
            # For now, only use emergency helplines from settings.py to avoid rate limiting
            priority_users = self.get_priority_users_for_emergency(max_users=0)
            
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

            # Email content for emergency helplines (PRIORITY EMAILS ONLY)
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
EMERGENCY NOTIFICATION: Sent to priority contacts only

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
            
            # 1. Send to affected passengers (if any)
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
            
            # 2. Skip user broadcast for now (only use emergency helplines)
            logger.info("Skipping user broadcast - using only emergency helplines from settings.py")
            
            # 3. Send to emergency helplines (PRIORITY EMAILS) (with small delays)
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
                    time.sleep(0.5)  # Small delay between helpline emails
                except Exception as e:
                    failed_emails.append(helpline_email)
                    logger.error(f"Failed to send email to helpline {helpline_email}: {str(e)}")
            
            # Log emergency notification
            self.log_emergency_notification(
                bus_number, latitude, longitude, 
                len(affected_passengers), len(priority_users), 
                emails_sent, failed_emails
            )
            
            return {
                'status': 'success',
                'emails_sent': emails_sent,
                'affected_passengers': len(affected_passengers),
                'broadcast_alerts': len(priority_users),
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
                                 affected_count, broadcast_count, emails_sent, failed_emails):
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
Emergency Broadcast Sent: {broadcast_count} users
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