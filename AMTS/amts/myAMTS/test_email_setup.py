#!/usr/bin/env python
"""
Test script to verify Gmail SMTP email configuration
Run this after setting up your Gmail App Password
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

def test_email_sending():
    """Test sending a real email through Gmail SMTP"""
    
    print("🔧 Testing Gmail SMTP Configuration...")
    print(f"📧 Email Backend: {settings.EMAIL_BACKEND}")
    print(f"📬 SMTP Host: {settings.EMAIL_HOST}")
    print(f"👤 Email User: {settings.EMAIL_HOST_USER}")
    print(f"🔐 Password Set: {'Yes' if settings.EMAIL_HOST_PASSWORD != 'your-16-digit-app-password' else 'NO - UPDATE REQUIRED'}")
    
    if settings.EMAIL_HOST_PASSWORD == 'your-16-digit-app-password':
        print("\n❌ ERROR: You need to update EMAIL_HOST_PASSWORD in settings.py")
        print("📋 Steps to get Gmail App Password:")
        print("   1. Go to Gmail → Account Settings → Security")
        print("   2. Enable 2-Step Verification (if not already enabled)")
        print("   3. Go to 2-Step Verification → App passwords")
        print("   4. Generate an app password for 'Mail'")
        print("   5. Copy the 16-digit password and update settings.py")
        return False
    
    try:
        # Send test email
        subject = "🚨 AMTS Emergency System - Email Test"
        message = """
        This is a test email from your AMTS Emergency Notification System.
        
        ✅ Gmail SMTP configuration is working correctly!
        
        System Details:
        - Email Backend: Gmail SMTP
        - Host: smtp.gmail.com
        - Port: 587
        - TLS: Enabled
        
        If you received this email, your emergency notification system is ready to send real alerts.
        
        Best regards,
        AMTS Emergency System
        """
        
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['vaibhavmevada796@gmail.com']
        
        print(f"\n📤 Sending test email to: {recipient_list[0]}")
        
        send_mail(
            subject=subject,
            message=message,
            from_email=from_email,
            recipient_list=recipient_list,
            fail_silently=False,
        )
        
        print("✅ SUCCESS: Test email sent successfully!")
        print("📬 Check your Gmail inbox for the test email")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: Failed to send email")
        print(f"🔍 Error details: {str(e)}")
        print("\n🛠️ Troubleshooting:")
        print("   1. Verify your Gmail App Password is correct")
        print("   2. Make sure 2-Step Verification is enabled on your Gmail")
        print("   3. Check if 'Less secure app access' is disabled (it should be)")
        print("   4. Ensure you're using the App Password, not your regular Gmail password")
        return False

if __name__ == "__main__":
    print("🚨 AMTS Emergency Email System Test")
    print("=" * 50)
    
    success = test_email_sending()
    
    if success:
        print("\n🎉 Email configuration is working!")
        print("💡 Your emergency notification system can now send real emails")
    else:
        print("\n⚠️  Please fix the configuration and try again")
    
    print("\n" + "=" * 50)