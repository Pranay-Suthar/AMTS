# AMTS - Ahmedabad Municipal Transport Service

> A comprehensive Django-based bus management system with real-time tracking, emergency safety notifications, and automated passenger services.

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
- [Bus Route Data Management](#bus-route-data-management)
- [Emergency Safety System](#emergency-safety-system)
- [Email Notification System](#email-notification-system)
- [Technology Stack](#technology-stack)
- [API Documentation](#api-documentation)
- [Security & Configuration](#security--configuration)
- [Support & Contact](#support--contact)

---

## Overview

AMTS is a modern, full-featured bus management system designed for the Ahmedabad Municipal Transport Service. The system provides real-time bus tracking, digital ticketing, automated bus pass generation, and a comprehensive emergency safety notification system.

### Project Statistics

- **29 Bus Routes** covering major areas of Ahmedabad
- **200+ Bus Stops** with accurate GPS coordinates
- **Real-time Tracking** for all active buses
- **Emergency Notification System** with multi-contact alerts
- **Automated Email Delivery** for passes and emergency alerts

---

## Key Features

### Core Bus Services

#### Real-Time Bus Tracking
- Live GPS location monitoring with interactive maps
- Multi-bus tracking on same route (Forward/Reverse directions)
- Speed monitoring and status updates
- Route visualization with all stops marked

#### Smart Route Planning
- Multi-route journey planning with transfer support
- Optimal route selection based on time and distance
- Stop-to-stop navigation with detailed instructions
- Real-time delay notifications

#### Digital Ticketing System
- Online ticket booking with secure payment processing
- QR code generation for digital verification
- Mobile-optimized ticket display
- Complete booking history and management

#### Bus Pass Management
- Monthly pass applications with automated processing
- Student pass system with academic verification
- Automated PDF generation and email delivery
- QR code integration for conductor verification

### Emergency Safety System

#### Instant Accident Detection
- One-click emergency alert activation from live tracking
- Automatic GPS coordinate capture and location freezing
- Real-time status updates on emergency dashboard
- Google Maps integration for precise location sharing

#### Multi-Channel Notifications
- Simultaneous email alerts to all emergency contacts
- Priority-based notification system (helplines first)
- Professional email templates with AMTS branding
- Real-time delivery confirmation and tracking

#### Visual Feedback System
- **Red Notifications**: Emergency alerts with pulsing animation
- **Green Notifications**: Success confirmations
- **Orange Notifications**: Important warnings
- **Blue Notifications**: General information

### Automated Email Systems

#### Bus Pass Delivery
- Automatic PDF generation upon pass approval
- Professional email templates with usage instructions
- Secure attachment delivery via Gmail SMTP
- Mobile-friendly PDF format

#### Emergency Notifications
- Real-time accident alerts with GPS coordinates
- Google Maps links for immediate location access
- Multi-recipient delivery (passengers, family, helplines)
- Delivery status tracking and confirmation

---

## System Requirements

### Prerequisites

- **Python**: 3.8 or higher
- **Django**: 5.2.10
- **Database**: SQLite (development) / PostgreSQL (production)
- **Email Service**: Gmail account with App Password
- **Operating System**: Windows, macOS, or Linux

### Python Dependencies

```
Django==5.2.10
python-dotenv==1.0.0
Pillow==10.1.0
qrcode==7.4.2
reportlab==4.0.7
```

---

## Installation Guide

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd AMTS/AMTS/amts/myAMTS
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration

Create a `.env` file in the project root directory:

```env
# Gmail Configuration
EMAIL_HOST_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-16-digit-app-password

# Django Security
SECRET_KEY=your-secret-key-here
DEBUG=True

# Database (Optional - defaults to SQLite)
DATABASE_URL=sqlite:///db.sqlite3
```

#### Gmail App Password Setup

1. Enable 2-Step Verification on your Gmail account
2. Navigate to: Google Account → Security → 2-Step Verification → App passwords
3. Generate password for "Mail" application
4. Copy the 16-digit password to your `.env` file

### Step 5: Database Setup

```bash
# Run migrations
python manage.py migrate

# Create superuser account
python manage.py createsuperuser
```

### Step 6: Load Bus Route Data

```bash
# Load all 29 bus routes from amts_data.json
python manage.py load_bus_data

# Or specify custom JSON file
python manage.py load_bus_data path/to/custom_routes.json
```

### Step 7: Start Development Server

```bash
python manage.py runserver
```

### Step 8: Access Application

- **Main Website**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Emergency Dashboard**: http://127.0.0.1:8000/emergency-dashboard/

---

## Bus Route Data Management

### Data Structure

The `amts_data.json` file contains comprehensive bus route information:

```json
[
  {
    "bus_number": "401",
    "stops": [
      {
        "name": "Vasna Terminus",
        "coordinates": [23.0075, 72.5159]
      },
      {
        "name": "Anandnagar",
        "coordinates": [23.0350, 72.5320]
      }
    ]
  }
]
```

### Management Command: load_bus_data

#### Features

- **Smart Upsert**: Creates new buses or updates existing ones without data loss
- **Data Validation**: Verifies bus numbers, stop names, and GPS coordinates
- **Flexible Loading**: Supports custom JSON files or built-in defaults
- **Progress Reporting**: Shows created/updated count for each operation

#### Usage

```bash
# Load from project's amts_data.json
python manage.py load_bus_data

# Load from custom file
python manage.py load_bus_data /path/to/routes.json

# View help
python manage.py load_bus_data --help
```

#### Command Output

```
Successfully created bus 401
Successfully updated bus 56
Successfully created bus 130
...
Operation Complete: 20 created, 8 updated.
```

### Included Bus Routes

| Bus No. | Route | Stops | Key Areas |
|---------|-------|-------|-----------|
| 401 | Vasna Terminus ↔ Chandkheda | 29 | Paldi, Usmanpura, Vadaj |
| 130 | Naroda ↔ Anjali Char Rasta | 16 | Ghodasar, Isanpur, Narol |
| 56 | Naroda ↔ Lal Darwaja | 11 | Thakkar Nagar, Kalupur |
| 58 | Thakkar Nagar ↔ Paldi | 12 | Bapu Nagar, Kalupur |
| 33 | Gokul Park ↔ Lal Darwaja | 12 | Khodiyar Nagar, Bombay Housing |
| 31_5 | Lal Darwaja ↔ LJ College | 11 | Vasna, Sarkhej, Sanand |
| 11 | Vadaj ↔ Maninagar | 9 | Usmanpura, Paldi, Kankaria |
| 89 | Chandkheda Gam ↔ Vastrapur | 8 | Motera, Sabarmati, Navrangpura |
| 1 | Maninagar ↔ Ghuma Gam | 10 | ISRO, Bopal, Sterling City |
| 160 | Gujarat High Court ↔ Hatkeshwar | 7 | Thaltej, Bopal, Sarkhej |

**Additional Routes**: 2, 3, 4, 5, 28, 49, 50, 61, 66, 69, 75, 83, 87, 101-105

### Coverage Areas

- **North Zone**: Naroda, Chandkheda, Motera, Sabarmati, Vadaj
- **South Zone**: Maninagar, Vasna, Sarkhej, Bopal, Ghuma
- **East Zone**: Ghodasar, Isanpur, Narol, Odhav, Nikol
- **West Zone**: Vastrapur, Thaltej, Science City, Sola, Bodakdev
- **Central Zone**: Paldi, Navrangpura, Kalupur, Lal Darwaja, Ashram Road

### GPS Coordinate System

All bus stops include accurate GPS coordinates for real-time tracking:

- **Latitude Range**: 22.95 to 23.12 (Ahmedabad city limits)
- **Longitude Range**: 72.46 to 72.67 (Ahmedabad city limits)
- **Coordinate Format**: `[latitude, longitude]`
- **Precision**: 4-5 decimal places for meter-level accuracy

---

## Emergency Safety System

### System Architecture

The emergency safety system provides instant accident detection and multi-channel notification capabilities with real-time status monitoring.

### Configuration

#### Emergency Contact List

Current priority contacts (configured in `settings.py`):

```python
EMERGENCY_HELPLINES = [
    'vaibhavmevada796@gmail.com',      # Primary Emergency Contact
    'paresh07suva@gmail.com',          # Emergency Contact - Paresh
    'emergency@amts.gov.in',           # AMTS Emergency Helpline
    'control.room@amts.gov.in',        # AMTS Control Room
    'safety@amts.gov.in',              # AMTS Safety Department
    'thakararyan9106@gmail.com',       # Emergency Contact - Aryan
    'admin@amts.gov.in'                # AMTS Admin
]
```

#### Email Backend Configuration

```python
# Gmail SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('GMAIL_APP_PASSWORD')
DEFAULT_FROM_EMAIL = 'AMTS Emergency <vaibhavmevada796@gmail.com>'
```

### Features

#### Accident Detection
- One-click emergency activation from live tracking interface
- Automatic GPS coordinate capture at accident location
- Bus status change to "OUT_OF_SERVICE"
- Location freezing for investigation purposes

#### Notification System
- **Priority-Based Delivery**: Emergency helplines notified first
- **Multi-Recipient Alerts**: Simultaneous email delivery
- **Professional Templates**: AMTS-branded emergency communications
- **GPS Integration**: Google Maps links for immediate location access
- **Real-Time Progress**: Visual progress bar showing email delivery status

#### Emergency Dashboard
- Live monitoring of all emergency situations
- Real-time status updates for active buses
- Emergency response coordination interface
- Historical accident data and analytics

### Testing Emergency System

#### Manual Testing

1. Navigate to bus search page
2. Search for any route (e.g., Naroda to Lal Darwaja)
3. Click "Live Track" button on search results
4. In the tracking modal, click "Simulate Accident" button
5. Confirm emergency alert activation
6. Monitor email progress bar showing delivery status
7. Check configured Gmail addresses for emergency notifications
8. Verify automatic redirect to Emergency Dashboard

#### Management Command Testing

```bash
# Test emergency notification system
python manage.py test_emergency
```

### Email Notification Content

Emergency emails include:

- Bus number and route information
- Precise GPS coordinates (latitude, longitude)
- Google Maps link for immediate navigation
- Timestamp of accident detection
- Affected passenger count
- Emergency contact instructions
- AMTS control room phone numbers

---

## Email Notification System

### Bus Pass Email Delivery

#### Automated PDF Generation

When a bus pass application is approved:

1. System generates professional PDF with pass details
2. PDF includes QR code for verification
3. Email is automatically sent to applicant's registered email
4. PDF is attached securely to the email

#### Email Template

```
Subject: Your AMTS Bus Pass is Ready

Dear [Applicant Name],

Your AMTS [Pass Type] has been approved and is ready for use.

Pass Details:
- Pass ID: [UUID]
- Valid From: [Start Date]
- Valid Until: [End Date]
- Route: [From Stop] to [To Stop]

Please find your bus pass attached as a PDF. You can:
- Save it on your mobile device
- Print a physical copy for backup
- Show it to the bus conductor when boarding

For support, contact: support@amts.gov.in

Best regards,
AMTS Team
```

### Emergency Email Delivery

#### Priority-Based Notification

Emergency emails are sent in priority order:

1. **Primary Emergency Contact** (vaibhavmevada796@gmail.com)
2. **Secondary Contacts** (paresh07suva@gmail.com, thakararyan9106@gmail.com)
3. **AMTS Emergency Services** (emergency@amts.gov.in)
4. **AMTS Control Room** (control.room@amts.gov.in)
5. **AMTS Safety Department** (safety@amts.gov.in)
6. **AMTS Administration** (admin@amts.gov.in)

#### Email Progress Tracking

Visual progress bar displays:
- Total emails to be sent
- Current email being sent
- Recipient email address or label
- Real-time percentage completion
- Success/failure status for each email

---

## Technology Stack

### Backend Framework

- **Django 5.2.10**: Python web framework with ORM
- **SQLite**: Development database (easily migrated to PostgreSQL)
- **Python 3.8+**: Core programming language

### Frontend Technologies

- **HTML5/CSS3**: Semantic markup and modern styling
- **Bootstrap 5**: Responsive UI framework
- **JavaScript ES6+**: Client-side functionality
- **Leaflet.js**: Interactive mapping and GPS visualization
- **AJAX**: Asynchronous data loading

### Third-Party Integrations

- **Gmail SMTP**: Email delivery service
- **ReportLab**: PDF generation library
- **QRCode**: QR code generation for tickets and passes
- **Pillow**: Image processing library
- **python-dotenv**: Environment variable management

### Security Features

- **CSRF Protection**: Cross-site request forgery prevention
- **Session Management**: Secure user authentication
- **Environment Variables**: Sensitive data protection
- **Input Validation**: Form data sanitization
- **SQL Injection Prevention**: Django ORM protection

---

## API Documentation

### Public Endpoints

#### Bus Search API

```
POST /api/search-buses/
Content-Type: application/json

Request:
{
  "from_stop": "Naroda",
  "to_stop": "Lal Darwaja"
}

Response:
{
  "direct_routes": [...],
  "transfer_routes": [...],
  "status": "success"
}
```

#### Active Buses API

```
GET /api/get-active-buses/?bus_number=56

Response:
{
  "buses": [
    {
      "identifier": "56-F1",
      "current_location": "Kalupur",
      "status": "ON_TIME",
      "speed": 45.0,
      "latitude": 23.03017,
      "longitude": 72.60041
    }
  ]
}
```

### Emergency System API

#### Trigger Emergency Notification

```
POST /api/emergency-accident/
Content-Type: application/json
X-CSRFToken: [token]

Request:
{
  "bus_number": "56",
  "accident_location": "Near Kalupur Station",
  "latitude": 23.03017,
  "longitude": 72.60041
}

Response:
{
  "status": "success",
  "emergency_response": {
    "notifications_sent": 7,
    "affected_passengers": 3,
    "helpline_alerts_sent": 7,
    "gps_coordinates": "23.03017, 72.60041",
    "google_maps_link": "https://www.google.com/maps?q=23.03017,72.60041",
    "bus_status": "OUT_OF_SERVICE",
    "location_frozen": true
  }
}
```

#### Update Bus Status

```
POST /api/update-bus-status/
Content-Type: application/json
X-CSRFToken: [token]

Request:
{
  "bus_id": "56-F1",
  "command": "manual_stop"
}

Response:
{
  "status": "success",
  "message": "Bus status updated"
}
```

---

## Security & Configuration

### Environment Variables

Required environment variables in `.env` file:

```env
# Django Configuration
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Database Configuration
DATABASE_URL=sqlite:///db.sqlite3

# Email Configuration
EMAIL_HOST_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-16-digit-app-password

# Optional: Email Backend Override
# EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
```

### Security Best Practices

#### Production Deployment

1. **Set DEBUG=False** in production environment
2. **Use PostgreSQL** instead of SQLite for production
3. **Configure ALLOWED_HOSTS** with your domain
4. **Use HTTPS** for all communications
5. **Implement rate limiting** for API endpoints
6. **Regular security updates** for all dependencies

#### Email Security

1. **Never commit** `.env` file to version control
2. **Use App Passwords** instead of account passwords
3. **Enable 2-Step Verification** on Gmail account
4. **Monitor email delivery** for suspicious activity
5. **Implement rate limiting** to prevent abuse

### Database Configuration

#### SQLite (Development)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

#### PostgreSQL (Production)

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'amts_db',
        'USER': 'amts_user',
        'PASSWORD': 'secure_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

---

## Application Routes

### Main Application

- `/` - Home page with bus search
- `/search/` - Advanced route search with live tracking
- `/my-bookings/` - User booking history
- `/login/` - User authentication
- `/register/` - New user registration
- `/logout/` - User logout

### Bus Pass System

- `/bus-pass/monthly/` - Monthly pass application
- `/bus-pass/student/` - Student pass application
- `/my-passes/` - User pass management

### Emergency System

- `/emergency-dashboard/` - Emergency monitoring dashboard
- `/api/emergency-accident/` - Emergency notification API
- `/api/update-bus-status/` - Bus status update API

### Admin Panel

- `/admin/` - Django admin interface
- `/admin/my_amts/bus/` - Bus management
- `/admin/my_amts/activebus/` - Active bus monitoring
- `/admin/my_amts/booking/` - Booking management
- `/admin/my_amts/buspass/` - Pass approval system

---

## Support & Contact

### Technical Support

- **Email**: support@amts.gov.in
- **Phone**: +91-79-2658-0000
- **Emergency Helpline**: 108

### AMTS Offices

- **Control Room**: control.room@amts.gov.in
- **Safety Department**: safety@amts.gov.in
- **Administration**: admin@amts.gov.in

### Development Team

- **Project Lead**: AMTS Development Team
- **Emergency System**: Safety Notification Specialist
- **Email Integration**: Gmail SMTP Expert
- **Frontend Design**: UI/UX Implementation Team

### Bug Reports & Feature Requests

For bug reports or feature requests:

1. Check existing issues in the repository
2. Provide detailed description with steps to reproduce
3. Include system logs and error messages
4. Specify Django version and Python version
5. Contact technical support for urgent issues

---

## Future Roadmap

### Phase 1: Mobile Integration
- Native iOS and Android applications
- Push notification system
- Mobile-optimized tracking interface
- Offline ticket storage

### Phase 2: Advanced Analytics
- AI-powered route optimization
- Predictive delay analysis
- Passenger flow forecasting
- Real-time capacity monitoring

### Phase 3: Communication Expansion
- SMS notification integration
- WhatsApp Business API integration
- Multi-language support (Gujarati, Hindi)
- Voice call emergency alerts

### Phase 4: System Expansion
- Multi-city support
- Third-party API integration
- Advanced reporting dashboard
- IoT sensor integration

---

## License & Credits

### Project Information

- **Project Name**: AMTS - Ahmedabad Municipal Transport Service
- **Version**: 2.0
- **Status**: Production Ready
- **Last Updated**: January 2026

### Developed For

Ahmedabad Municipal Transport Service  
Next-generation bus management system with emergency-ready capabilities

### Acknowledgments

- Django Software Foundation for the excellent web framework
- Leaflet.js for interactive mapping capabilities
- Bootstrap team for responsive UI components
- ReportLab for PDF generation capabilities

---

**For more information, visit the AMTS website or contact technical support.**
