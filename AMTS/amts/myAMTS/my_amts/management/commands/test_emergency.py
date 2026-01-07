# my_amts/management/commands/test_emergency.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from my_amts.models import Bus, ActiveBus, Booking
from my_amts.emergency_notifications import EmergencyNotificationSystem
from datetime import datetime

class Command(BaseCommand):
    help = 'Test the Emergency Accident Notification System'

    def add_arguments(self, parser):
        parser.add_argument(
            '--bus-number',
            type=str,
            default='45',
            help='Bus number for testing (default: 45)'
        )
        parser.add_argument(
            '--create-test-data',
            action='store_true',
            help='Create test users and bookings'
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('🚨 AMTS Emergency Accident Notification System - Test')
        )
        self.stdout.write('=' * 60)

        bus_number = options['bus_number']
        
        if options['create_test_data']:
            self.create_test_data()

        # Test emergency system
        self.test_emergency_system(bus_number)

    def create_test_data(self):
        """Create test users and bookings"""
        self.stdout.write('\n🔧 Creating test data...')
        
        # Create test users
        test_users = [
            {'username': 'john_doe', 'email': 'john.doe@example.com', 'first_name': 'John', 'last_name': 'Doe'},
            {'username': 'jane_smith', 'email': 'jane.smith@example.com', 'first_name': 'Jane', 'last_name': 'Smith'},
            {'username': 'raj_patel', 'email': 'raj.patel@example.com', 'first_name': 'Raj', 'last_name': 'Patel'},
            {'username': 'priya_shah', 'email': 'priya.shah@example.com', 'first_name': 'Priya', 'last_name': 'Shah'},
            {'username': 'amit_kumar', 'email': 'amit.kumar@example.com', 'first_name': 'Amit', 'last_name': 'Kumar'},
        ]
        
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
                self.stdout.write(f'✅ Created user: {user.username} ({user.email})')

        # Create test bookings
        users_with_bookings = User.objects.filter(username__in=['john_doe', 'jane_smith', 'raj_patel'])
        for user in users_with_bookings:
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
                self.stdout.write(f'✅ Created booking for {user.username} on Bus 45')

        self.stdout.write(self.style.SUCCESS('✅ Test data created successfully!'))

    def test_emergency_system(self, bus_number):
        """Test the emergency notification system"""
        self.stdout.write(f'\n🚨 Testing Emergency System for Bus {bus_number}')
        self.stdout.write('-' * 40)
        
        # Test coordinates (Ahmedabad)
        latitude = 23.0225
        longitude = 72.5714
        accident_location = "Near Paldi Bus Stop, Ahmedabad"
        
        self.stdout.write(f'🚌 Bus Number: {bus_number}')
        self.stdout.write(f'📍 Location: {accident_location}')
        self.stdout.write(f'🌐 GPS: {latitude}, {longitude}')
        
        # Initialize emergency system
        emergency_system = EmergencyNotificationSystem()
        
        # Send notifications
        self.stdout.write(f'\n📧 Sending emergency notifications...')
        result = emergency_system.send_emergency_emails(
            bus_number=bus_number,
            latitude=latitude,
            longitude=longitude,
            accident_location=accident_location
        )
        
        # Display results
        self.stdout.write(f'\n📊 RESULTS:')
        if result['status'] == 'success':
            self.stdout.write(self.style.SUCCESS(f'✅ Status: SUCCESS'))
            self.stdout.write(f'📧 Total Emails: {result["emails_sent"]}')
            self.stdout.write(f'👥 Affected Passengers: {result["affected_passengers"]}')
            self.stdout.write(f'👨‍👩‍👧‍👦 Family Alerts: {result["family_alerts"]}')
            self.stdout.write(f'🚨 Helpline Alerts: {result["helpline_alerts"]}')
            
            if result['failed_emails']:
                self.stdout.write(self.style.WARNING(f'⚠️ Failed Emails: {len(result["failed_emails"])}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'✅ All emails sent successfully!'))
                
        else:
            self.stdout.write(self.style.ERROR(f'❌ Status: FAILED'))
            self.stdout.write(self.style.ERROR(f'Error: {result.get("message")}'))
        
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(self.style.SUCCESS('🔍 Check console output above for email content'))
        self.stdout.write(self.style.SUCCESS('📁 Check logs/emergency_notifications.log for detailed logs'))
        
        # Instructions
        self.stdout.write(f'\n🌐 WEB INTERFACE:')
        self.stdout.write(f'Visit: http://127.0.0.1:8000/emergency-dashboard/')
        self.stdout.write(f'API Endpoint: http://127.0.0.1:8000/api/emergency-accident/')