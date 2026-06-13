# UrbanTransit Web — Municipal Transport Management Platform

> A real-time bus tracking and automated passenger service system built for the Ahmedabad Municipal Transport Service (AMTS), covering 51 routes and 400+ stops.

**Built with** Python · Django · SQLite · Gmail SMTP · Leaflet.js

---

## What is UrbanTransit Web?

Municipal bus networks in India often lack a unified digital platform. Passengers have no reliable way to track buses in real time, book tickets digitally, or receive instant emergency alerts when incidents occur on routes.

UrbanTransit Web addresses this gap with a full-stack Django backend that handles live route tracking across 51 AMTS bus lines, automated QR ticket generation via SMTP, and an incident response system that fires emergency alerts to multiple contacts with coordinate-level telemetry — all within a session-isolated, CSRF-protected architecture.

---

## Core Features

### Real-Time Tracking
- Live GPS monitoring across 51 bus routes and 400+ designated stops
- Interactive maps powered by Leaflet.js with route visualization
- Active bus lookup by route number via REST API

### Digital Ticketing
- Online booking with instant QR code generation
- Automated SMTP pipeline delivers scannable ticket receipts to passenger email
- Bus pass system with auto-generated PDF documents via ReportLab

### Emergency Response System
- Incident alert API accepts coordinate telemetry (latitude/longitude) from buses
- Fires simultaneous email notifications to multiple emergency contacts (AMTS control room, safety department, admin)
- Redirects to a live Emergency Dashboard for real-time incident tracking
- Built-in session isolation ensures 100% data vector security per incident event

### Route Intelligence
- 51 comprehensive routes covering all major zones of Ahmedabad
- Multi-route journey planning with transfer support
- Smart stop search: find routes between any two stops in the network

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 5.2.10, Python 3.8+ |
| Database | SQLite (dev) / PostgreSQL (prod) |
| Frontend | HTML5, CSS3, Bootstrap 5, JavaScript ES6+, Leaflet.js |
| Email | Gmail SMTP (App Password auth) |
| PDF & QR | ReportLab, QRCode, Pillow |
| Security | CSRF Protection, Session Management, Environment Variables |

---

## Getting Started

### Prerequisites
- Python 3.8+
- Django 5.2.10
- Gmail account with App Password enabled

### Installation

```bash
# Clone and navigate to project
cd AMTS/AMTS/amts/myAMTS

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (.env)
EMAIL_HOST_USER=your-email@gmail.com
GMAIL_APP_PASSWORD=your-16-digit-app-password
SECRET_KEY=your-secret-key
DEBUG=True

# Run database migrations
python manage.py migrate
python manage.py createsuperuser

# Load all 51 bus routes and 400+ stops
python manage.py load_bus_data amts_data.json

# Start the development server
python manage.py runserver
```

### Access Points

| Panel | URL |
|---|---|
| Main Site | http://127.0.0.1:8000/ |
| Admin Panel | http://127.0.0.1:8000/admin/ |
| Emergency Dashboard | http://127.0.0.1:8000/emergency-dashboard/ |

### Gmail SMTP Setup
1. Enable 2-Step Verification on your Gmail account
2. Navigate to **Account → Security → App Passwords**
3. Generate a 16-digit App Password
4. Add it to your `.env` file as `GMAIL_APP_PASSWORD`

---

## API Endpoints

```bash
# Search buses between two stops
POST /api/search-buses/
Body: {"from_stop": "Naroda", "to_stop": "Lal Darwaja"}

# Get active buses on a route
GET /api/get-active-buses/?bus_number=56

# Trigger emergency alert with coordinates
POST /api/emergency-accident/
Body: {"bus_number": "56", "latitude": 23.03017, "longitude": 72.60041}
```

---

## Route Coverage

51 routes covering all major zones of Ahmedabad:

| Zone | Key Areas |
|---|---|
| North | Naroda, Chandkheda, Motera, Sabarmati, Gota |
| South | Maninagar, Vasna, Sarkhej, Bopal, Ghuma |
| East | Ghodasar, Isanpur, Narol, Nikol, Odhav, Vastral |
| West | Satellite, Vastrapur, Thaltej, Science City, Sola |
| Central | Paldi, Navrangpura, Kalupur, Lal Darwaja, CG Road |

Longest route: **401 — Vasna Terminus ↔ Chandkheda** (29 stops)

---

## Project Structure

```
AMTS/
├── my_amts/
│   ├── models.py                      # Route, stop, booking models
│   ├── views.py                       # View controllers
│   ├── urls.py                        # URL routing
│   ├── emergency_notifications.py     # Incident alert system
│   └── templates/                     # HTML templates
├── myAMTS/
│   └── settings.py                    # Project configuration
├── amts_data.json                     # Bus route dataset (51 routes, 400+ stops)
├── db.sqlite3                         # SQLite database
├── manage.py
└── requirements.txt
```

---

## Emergency System — Contact Configuration

```python
# settings.py
EMERGENCY_HELPLINES = [
    'primary.contact@example.com',
    'emergency@amts.gov.in',
    'control.room@amts.gov.in',
    'safety@amts.gov.in',
    'admin@amts.gov.in'
]
```

---

**Version**: 2.1 | **Status**: Production Ready | **Updated**: January 2026  
**Routes**: 51 | **Stops**: 400+ | **Coverage**: Complete Ahmedabad
