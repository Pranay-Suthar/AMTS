#!/usr/bin/env python
"""
Test script to verify Gmail SMTP email configuration
Now testing with your actual Gmail App Password
"""

import os
import sys
import django
from django.core.mail import send_mail
from django.conf import settings

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myAMTS.settings')
django.setup()

def test_gmail_smtp():
    """Test sending real email through Gmail SMTP"""
    
    print("🚨 AMTS Emergency Email System - Gmail SMTP Test")
    print("=" * 50)
    print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
    print(f"📬 SMTP Host: {settings.EMAIL_HOST}")
    print(f"👤 Email User: {settings.EMAIL_HOST_USER}")
    print(f"🔐 App Password: {'✅ Set' if settings.EMAIL_HOST_PASSWORD != 'your-16-digit-app-password' else '❌ Not Set'}")
    
    try:
        # Send test email
        subject = "🚨 AMTS Emergency System - Real Email Test"
        message = """
🎉 SUCCESS! Your AMTS Emergency Notification System is working!

✅ Gmail SMTP Configuration Active
✅ Real emails are now being sent to your Gmail
✅ Emergency alerts will be delivered instantly

System Details:
- Email Backend: Gmail SMTP
- Host: smtp.gmail.com
- Port: 587 (TLS Enabled)
- From: vaibhavmevada796@gmail.com

🚨 Emergency Features Ready:
- Bus accident alerts
- Emergency stop notifications  
- Traffic updates
- Service disruptions
- Real-time location alerts

This confirms your emergency notification system can send real emails to vaibhavmevada796@gmail.com

Best regards,
AMTS Emergency System
        """
        
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['vaibhavmevada796@gmail.com']
        
        print(f"\n📤 Sending real email to: {recipient_list[0]}")
        print("⏳ Connecting to Gmail SMTP...")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        print("✅ SUCCESS: Real email sent to your Gmail!")
        print("📬 Check your Gmail inbox - you should receive the email within seconds")
        print("🎯 Your emergency notification system is now LIVE!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: Failed to send email")
        print(f"🔍 Error details: {str(e)}")
        print("\n🛠️ Troubleshooting:")
        print("   1. Check your internet connection")
        print("   2. Verify the App Password is correct: vaqy fguy taat oiaj")
        print("   3. Make sure 2-Step Verification is still enabled")
        print("   4. Try generating a new App Password if needed")
        return False

def test_emergency_alert():
    """Send a sample emergency alert"""
    
    print("\n🚨 Testing Emergency Alert...")
    
    try:
        subject = "🚨 EMERGENCY - Bus Accident Alert"
        message = """
URGENT: EMERGENCY NOTIFICATION

🚨 BUS ACCIDENT DETECTED 🚨

Details:
- Bus: GJ-01-AB-1234
- Route: Ahmedabad Central → ISRO
- Location: Satellite Road, Near ISRO
- Time: 2026-01-27 16:45 IST
- Status: Emergency services dispatched

Actions Taken:
✅ Police notified
✅ Ambulance dispatched  
✅ Traffic diverted
✅ Backup bus sent

Emergency Helpline: +91-79-1234-5678

This is an automated alert from AMTS Emergency System.
        """
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=['vaibhavmevada796@gmail.com'],
            fail_silently=False,
        )
        
        print("✅ Emergency alert sent successfully!")
        print("📧 Check your Gmail for the emergency notification")
        
    except Exception as e:
        print(f"❌ Emergency alert failed: {str(e)}")

if __name__ == "__main__":
    success = test_gmail_smtp()
    
    if success:
        test_emergency_alert()
        print("\n" + "=" * 50)
        print("🎉 CONGRATULATIONS!")
        print("📧 Your AMTS Emergency System can now send REAL emails!")
        print("🚨 All emergency alerts will be delivered to: vaibhavmevada796@gmail.com")
        print("⚡ System is LIVE and ready for emergency notifications!")
    else:
        print("\n⚠️ Please check the configuration and try again")
    
    print("\n" + "=" * 50)