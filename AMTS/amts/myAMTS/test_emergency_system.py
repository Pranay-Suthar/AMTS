#!/usr/bin/env python
"""
Emergency Accident Notification System - Test Script
Run this to test the emergency system locally
"""

import os
import sys
import django
import requests
import json

# Setup Django environment
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAMTS.settings')
django.setup()

from django.contrib.auth.models import User
from my_amts.models import Bus, ActiveBus, Booking
from my_amts.emergency_notifications import EmergencyNotificationSystem

def create_test_data():
    """Create test users and bookings for demonstration"""
    print("🔧 Setting up test data...")
    
    # Create test users with emails
    test_users = [
        {'username': 'john_doe', 'email': 'john.doe@example.com', 'first_name': 'John', 'last_name': 'Doe'},
        {'username': 'jane_smith', 'email': 'jane.smith@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
        {'username': 'raj_patel', 'email': 'raj.patel@example.com', 'first_name': 'Raj', 'last_name': 'Patel'},
        {'username': 'priya_shah', 'email': 'priya.shah@example.com', 'first_name': 'Priya', 'last_name': 'Shah'},
        {'username': 'amit_kumar', 'email': 'amit.kumar@example.com', 'first_name': 'Amit', 'last_name': 'Kumar'},
    ]
    
    created_users = []
    for user_data in test_users:
        user, created = User.objects.get_or_create(
            username=user_data['username'],
            defaults={
                'email': user_data['email'],
                'first_name': user_data['first_name'],
                'last_name': user_data['last_name'],
                'is_active': True
            }
        )
        if created:
            user.set_password('testpass123')
            user.save()
            print(f"✅ Created user: {user.username} ({user.email})")
        created_users.append(user)
    
    # Create test bookings for bus 45
    from datetime import datetime
    for i, user in enumerate(created_users[:3]):  # First 3 users have bookings
        booking, created = Booking.objects.get_or_create(
            user=user,
            bus_number='45',
            defaults={
                'from_stop': 'Paldi',
                'to_stop': 'Maninagar',
                'total_amount': 15.00,
                'payment_status': 'COMPLETED'
            }
        )
        if created:
            print(f"✅ Created booking for {user.username} on Bus 45")
    
    print(f"✅ Test data setup complete!")
    return created_users

def test_emergency_system():
    """Test the emergency notification system"""
    print("\n🚨 TESTING EMERGENCY ACCIDENT NOTIFICATION SYSTEM 🚨")
    print("=" * 60)
    
    # Test data
    bus_number = "45"
    latitude = 23.0225  # Ahmedabad coordinates
    longitude = 72.5714
    accident_location = "Near Paldi Bus Stop, Ahmedabad"
    
    print(f"🚌 Bus Number: {bus_number}")
    print(f"📍 Accident Location: {accident_location}")
    print(f"🌐 GPS Coordinates: {latitude}, {longitude}")
    print(f"🔗 Google Maps: https://www.google.com/maps?q={latitude},{longitude}")
    
    # Initialize emergency system
    emergency_system = EmergencyNotificationSystem()
    
    # Send emergency notifications
    print(f"\n📧 Sending emergency notifications...")
    result = emergency_system.send_emergency_emails(
        bus_number=bus_number,
        latitude=latitude,
        longitude=longitude,
        accident_location=accident_location
    )
    
    # Display results
    print(f"\n📊 EMERGENCY NOTIFICATION RESULTS:")
    print(f"=" * 40)
    
    if result['status'] == 'success':
        print(f"✅ Status: SUCCESS")
        print(f"📧 Total Emails Sent: {result['emails_sent']}")
        print(f"👥 Affected Passengers: {result['affected_passengers']}")
        print(f"👨‍👩‍👧‍👦 Family Alerts: {result['family_alerts']}")
        print(f"🚨 Helpline Alerts: {result['helpline_alerts']}")
        
        if result['failed_emails']:
            print(f"❌ Failed Emails: {len(result['failed_emails'])}")
            for email in result['failed_emails']:
                print(f"   - {email}")
        else:
            print(f"✅ All emails sent successfully!")
        
        print(f"\n🚨 ACCIDENT DETAILS:")
        details = result['accident_details']
        print(f"   Bus: {details['bus_number']}")
        print(f"   Route: {details['route']}")
        print(f"   Location: {details['location']}")
        print(f"   Maps Link: {details['maps_link']}")
        print(f"   Time: {details['timestamp']}")
        
    else:
        print(f"❌ Status: FAILED")
        print(f"❌ Error: {result.get('message', 'Unknown error')}")
    
    print(f"\n" + "=" * 60)
    print(f"🔍 Check your console for email outputs (using console backend)")
    print(f"📁 Check logs/emergency_notifications.log for detailed logs")

def test_api_endpoint():
    """Test the API endpoint (requires Django server running)"""
    print(f"\n🌐 TESTING API ENDPOINT")
    print(f"=" * 30)
    
    # Test data
    test_data = {
        'bus_number': '45',
        'latitude': 23.0225,
        'longitude': 72.5714,
        'accident_location': 'Near Paldi Bus Stop, Ahmedabad'
    }
    
    try:
        # Try to call the API endpoint
        response = requests.post(
            'http://127.0.0.1:8000/api/emergency-accident/',
            json=test_data,
            headers={'Content-Type': 'application/json'},
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print(f"✅ API Test: SUCCESS")
            print(f"📧 Notifications Sent: {result['emergency_response']['notifications_sent']}")
            print(f"🚌 Bus Status: {result['emergency_response']['bus_status']}")
            print(f"📍 Location Frozen: {result['emergency_response']['location_frozen']}")
        else:
            print(f"❌ API Test: FAILED (Status: {response.status_code})")
            print(f"Response: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print(f"⚠️ API Test: Server not running at http://127.0.0.1:8000/")
        print(f"   Start Django server with: python manage.py runserver")
    except Exception as e:
        print(f"❌ API Test: ERROR - {str(e)}")

if __name__ == "__main__":
    print("🚨 AMTS Emergency Accident Notification System - Test Suite")
    print("=" * 65)
    
    # Create test data
    users = create_test_data()
    
    # Test emergency system directly
    test_emergency_system()
    
    # Test API endpoint
    test_api_endpoint()
    
    print(f"\n🎯 TESTING COMPLETE!")
    print(f"📧 All emails are logged to console (EMAIL_BACKEND = console)")
    print(f"🔍 Check the Django console output for email content")
    print(f"📁 Emergency logs saved to: logs/emergency_notifications.log")
    
    print(f"\n🚀 TO USE IN PRODUCTION:")
    print(f"1. Update EMAIL_BACKEND in settings.py to use real SMTP")
    print(f"2. Configure SMS gateway for SMS notifications")
    print(f"3. Update emergency helpline email addresses")
    print(f"4. Test with real email addresses")