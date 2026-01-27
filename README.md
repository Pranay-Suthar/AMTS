# 🚌 AMTS - Ahmedabad Municipal Transport Service

A comprehensive Django-based bus management system with real-time tracking, emergency notifications, and passenger services.

## ✨ Features

### 🚌 **Core Bus Services**
- **Real-time Bus Tracking** - Live GPS location and status
- **Route Planning** - Multi-route journey planning with transfers
- **Ticket Booking** - Online ticket booking with QR codes
- **Bus Pass System** - Monthly and student pass applications

### 🚨 **Emergency System**
- **Accident Detection** - Instant emergency alert system
- **Real Email Notifications** - Gmail SMTP integration
- **Emergency Dashboard** - Live emergency status monitoring
- **GPS Location Freezing** - Accident location tracking

### 👤 **User Management**
- **User Authentication** - Secure login/registration
- **Booking History** - Track all bookings and passes
- **Search History** - Recent route searches

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Django 5.2+
- Gmail account with App Password

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd AMTS/AMTS/amts/myAMTS
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create `.env` file:
   ```env
   GMAIL_APP_PASSWORD=your-16-digit-app-password
   EMAIL_HOST_USER=your-email@gmail.com
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```

5. **Load Sample Data**
   ```bash
   python manage.py loaddata bus_data.json
   ```

6. **Run the Server**
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**
   - Main Site: http://127.0.0.1:8000/
   - Emergency Dashboard: http://127.0.0.1:8000/emergency-dashboard/
   - Admin Panel: http://127.0.0.1:8000/admin/

## 🚨 Emergency System Setup

### Gmail Configuration
1. Enable 2-Step Verification on your Gmail
2. Generate App Password: Gmail → Security → 2-Step Verification → App passwords
3. Add the 16-digit password to your `.env` file

### Testing Emergency System
1. Go to any bus route search
2. Click "🚨 Simulate Accident" button
3. Confirm the emergency alert
4. Check your Gmail for emergency notifications

## 📧 Email Recipients
- Primary: Your Gmail address
- Test: cipaha2099@gxuzi.com
- Emergency helplines (4 configured addresses)

## 🛠️ Technology Stack
- **Backend**: Django 5.2.10
- **Database**: SQLite (development)
- **Email**: Gmail SMTP
- **Frontend**: HTML, CSS, JavaScript
- **QR Codes**: qrcode library
- **PDF Generation**: ReportLab

## 📱 Key URLs
- `/` - Home page with bus search
- `/search/` - Advanced bus route search
- `/emergency-dashboard/` - Emergency management
- `/my-bookings/` - User booking history
- `/bus-pass/monthly/` - Monthly pass application
- `/bus-pass/student/` - Student pass application

## 🔒 Security Features
- Environment variable configuration
- CSRF protection
- User authentication
- Secure email handling

## 🚌 Bus System Features
- **Live Tracking**: Real-time bus locations
- **Route Optimization**: Multi-transfer journey planning
- **QR Ticketing**: Digital ticket generation
- **Emergency Alerts**: Instant accident notifications

## 📊 Emergency Dashboard
- Active emergency monitoring
- GPS location tracking
- Email notification status
- Emergency response coordination

## 🎯 Future Enhancements
- SMS notifications
- Mobile app integration
- Advanced analytics
- Multi-language support

---

**Developed for Ahmedabad Municipal Transport Service**  
*Emergency-ready bus management system with real-time capabilities*