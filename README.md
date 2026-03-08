# AMTS - Ahmedabad Municipal Transport Service

> Modern bus management system with real-time tracking, emergency notifications, and automated passenger services.

---

## Features

- **Real-Time Bus Tracking** - Live GPS monitoring with interactive maps
- **Smart Route Planning** - Multi-route journey planning with transfers
- **Digital Ticketing** - Online booking with QR code generation
- **Bus Pass System** - Automated PDF generation and email delivery
- **Emergency Safety System** - Instant accident alerts with multi-contact notifications
- **Email Automation** - Gmail SMTP integration for passes and emergency alerts

---

## Quick Start

### Prerequisites

- Python 3.8+
- Django 5.2.10
- Gmail account with App Password

### Installation

```bash
# Clone and navigate
cd AMTS/AMTS/amts/myAMTS

# Install dependencies
pip install -r requirements.txt

# Configure environment (.env file)
EMAIL_HOST_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-16-digit-app-password
SECRET_KEY=your-secret-key
DEBUG=True

# Setup database
python manage.py migrate
python manage.py createsuperuser

# Load bus routes (29 routes, 200+ stops)
python manage.py load_bus_data

# Start server
python manage.py runserver
```

### Access Points

- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/
- **Emergency Dashboard**: http://127.0.0.1:8000/emergency-dashboard/

---

## Bus Route Data

### Available Routes

29 bus routes covering Ahmedabad with 200+ stops including:

| Bus | Route | Stops |
|-----|-------|-------|
| 401 | Vasna Terminus ↔ Chandkheda | 29 |
| 130 | Naroda ↔ Anjali Char Rasta | 16 |
| 56 | Naroda ↔ Lal Darwaja | 11 |
| 58 | Thakkar Nagar ↔ Paldi | 12 |
| 33 | Gokul Park ↔ Lal Darwaja | 12 |
| 31_5 | Lal Darwaja ↔ LJ College | 11 |

**Additional routes**: 1, 2, 3, 4, 5, 11, 28, 49, 50, 61, 66, 69, 75, 83, 87, 89, 101-105, 160

### Coverage Areas

- **North**: Naroda, Chandkheda, Motera, Sabarmati
- **South**: Maninagar, Vasna, Sarkhej, Bopal
- **East**: Ghodasar, Isanpur, Narol, Odhav
- **West**: Vastrapur, Thaltej, Science City, Sola
- **Central**: Paldi, Navrangpura, Kalupur, Lal Darwaja

---

## Emergency System

### Configuration

Emergency contacts (configured in `settings.py`):

```python
EMERGENCY_HELPLINES = [
    'primary.contact@example.com',   # Primary Contact
    'emergency@amts.gov.in',         # AMTS Emergency
    'control.room@amts.gov.in',      # Control Room
    'safety@amts.gov.in',            # Safety Department
    'admin@amts.gov.in'              # Admin
]
```

### Gmail Setup

1. Enable 2-Step Verification on Gmail
2. Generate App Password: Account → Security → App passwords
3. Add 16-digit password to `.env` file

### Testing

1. Search for any bus route
2. Click "Live Track" button
3. Click "Simulate Accident" in tracking modal
4. Monitor email progress bar
5. Check Gmail for emergency notifications
6. Verify redirect to Emergency Dashboard

---

## Technology Stack

**Backend**: Django 5.2.10, SQLite/PostgreSQL, Python 3.8+  
**Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript ES6+, Leaflet.js  
**Integrations**: Gmail SMTP, ReportLab (PDF), QRCode, Pillow  
**Security**: CSRF Protection, Session Management, Environment Variables

---

## API Endpoints

### Bus Search
```bash
POST /api/search-buses/
{"from_stop": "Naroda", "to_stop": "Lal Darwaja"}
```

### Active Buses
```bash
GET /api/get-active-buses/?bus_number=56
```

### Emergency Alert
```bash
POST /api/emergency-accident/
{"bus_number": "56", "latitude": 23.03017, "longitude": 72.60041}
```

---

## Project Structure

```
AMTS/
├── my_amts/                    # Main application
│   ├── models.py              # Database models
│   ├── views.py               # View controllers
│   ├── urls.py                # URL routing
│   ├── emergency_notifications.py  # Emergency system
│   └── templates/             # HTML templates
├── myAMTS/                    # Project settings
│   └── settings.py            # Configuration
├── media/                     # Uploaded files
├── amts_data.json            # Bus route data
├── db.sqlite3                # Database
├── manage.py                 # Django management
└── requirements.txt          # Dependencies
```

---

## Support

**Technical Support**: support@amts.gov.in  
**Emergency Helpline**: +91-79-2658-0000  
**Control Room**: control.room@amts.gov.in

---

**Version**: 2.0 | **Status**: Production Ready | **Updated**: January 2026

Developed for Ahmedabad Municipal Transport Service
