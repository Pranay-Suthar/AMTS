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

# Load bus routes (51 routes, 400+ stops)
python manage.py load_bus_data amts_data.json

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

51 comprehensive bus routes covering all major areas of Ahmedabad with 400+ stops:

| Bus | Route | Stops | Coverage |
|-----|-------|-------|----------|
| 401 | Vasna Terminus ↔ Chandkheda | 29 | Longest Route |
| 130 | Naroda ↔ Anjali Char Rasta | 16 | East Zone |
| 56 | Naroda ↔ Lal Darwaja | 11 | North-Central |
| 58 | Thakkar Nagar ↔ Paldi | 12 | Central |
| 33 | Gokul Park ↔ Lal Darwaja | 12 | East-Central |
| 31_5 | Lal Darwaja ↔ LJ College | 11 | South-West |
| 6 | Satellite ↔ Gujarat University | 8 | Premium West |
| 7 | SG Highway ↔ Chandkheda | 8 | SG Highway Corridor |
| 8 | Maninagar Railway ↔ Mithakhali | 8 | East-West |
| 9 | Naranpura ↔ Ashram Road | 8 | North-Central |
| 10 | Nikol ↔ Kalupur Railway | 8 | Industrial East |

**All routes**: 1-10, 11-30, 31_5, 33, 49-50, 56, 58, 61, 66, 69, 75, 83, 87, 89, 101-105, 130, 160, 401

### Coverage Areas

**Premium & Commercial Zones:**
- **SG Highway Corridor**: Prahlad Nagar, Bodakdev, Satellite, Shapath Hexa
- **CG Road Area**: Ambawadi, Memnagar, Law Garden, Parimal Garden
- **West Ahmedabad**: Vastrapur, Thaltej, Science City, Sola, Ghatlodia

**Residential Areas:**
- **North**: Naroda, Chandkheda, Motera, Sabarmati, Gota, Sargasan
- **South**: Maninagar, Vasna, Sarkhej, Bopal, Ghuma
- **East**: Ghodasar, Isanpur, Narol, Nikol, Odhav, Vastral
- **Central**: Paldi, Navrangpura, Kalupur, Lal Darwaja, Ellisbridge

**Key Landmarks:**
- Railway Stations: Maninagar, Kalupur
- Educational: Gujarat University, LD Engineering College
- Commercial: CG Road, Ashram Road, Relief Road
- Recreation: Kankaria Lake, Vastrapur Lake, Science City

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

**Version**: 2.1 | **Status**: Production Ready | **Updated**: January 2026  
**Bus Routes**: 51 | **Bus Stops**: 400+ | **Coverage**: Complete Ahmedabad

Developed for Ahmedabad Municipal Transport Service
