# 🚌 AMTS - Ahmedabad Municipal Transport Service

A comprehensive Django-based bus management system with **real-time tracking**, **emergency safety notifications**, and **automated passenger services**.

## ✨ Key Features

### 🚌 **Core Bus Services**
- **Real-time Bus Tracking** - Live GPS location and status monitoring
- **Smart Route Planning** - Multi-route journey planning with transfers
- **Digital Ticket Booking** - Online ticket booking with QR code generation
- **Bus Pass System** - Monthly and student pass applications with PDF delivery
- **Automated Email Delivery** - Bus passes sent directly to user email

### 🚨 **Advanced Emergency Safety System**
- **Instant Accident Detection** - One-click emergency alert activation
- **Real Gmail SMTP Integration** - Live email notifications to emergency contacts
- **Color-Coded Visual Feedback** - Red/Green/Orange notification system
- **Emergency Dashboard** - Live emergency status monitoring and control
- **GPS Location Freezing** - Automatic accident location tracking and Google Maps integration
- **Multi-Contact Notification** - Simultaneous alerts to passengers, family, and emergency services

### 📧 **Automated Email Systems**
- **Bus Pass PDF Delivery** - Automatic email delivery of generated bus passes
- **Emergency Notifications** - Real-time accident alerts with GPS coordinates
- **Professional Email Templates** - AMTS-branded email communications
- **Gmail App Password Integration** - Secure email delivery system

### 👤 **User Management & History**
- **Secure Authentication** - User login/registration with session management
- **Booking History** - Complete tracking of all bookings and passes
- **Search History** - Recent route searches with quick access
- **Personal Dashboard** - User-specific booking and pass management

## 🚀 Quick Start Guide

### Prerequisites
- **Python 3.8+** - Latest Python version recommended
- **Django 5.2.10** - Web framework
- **Gmail Account** - With 2-Step Verification and App Password
- **Git** - For version control

### Installation Steps

1. **Clone the Repository**
   ```bash
   git clone <your-repo-url>
   cd AMTS/AMTS/amts/myAMTS
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**
   Create `.env` file in project root:
   ```env
   # Gmail Configuration for Email Delivery
   GMAIL_APP_PASSWORD=your-16-digit-app-password
   EMAIL_HOST_USER=your-email@gmail.com
   
   # Security Settings
   SECRET_KEY=your-secret-key
   DEBUG=True
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py loaddata amts_data.json  # Load sample bus data
   ```

5. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

6. **Access Application**
   - **Main Website**: http://127.0.0.1:8000/
   - **Emergency Dashboard**: http://127.0.0.1:8000/emergency-dashboard/
   - **Admin Panel**: http://127.0.0.1:8000/admin/

## 🚨 Emergency Safety System

### 📧 Gmail SMTP Configuration
1. **Enable 2-Step Verification** on your Gmail account
2. **Generate App Password**: 
   - Go to Gmail → Account Settings → Security → 2-Step Verification → App passwords
   - Create password for "Mail" application
3. **Add to Environment**: Add the 16-digit password to your `.env` file
4. **Test Configuration**: Use the built-in email test system

### 🔴 Emergency System Features
- **One-Click Activation** - Instant emergency alert from live tracking
- **GPS Coordinate Capture** - Automatic location freezing at accident point
- **Multi-Contact Notification** - Simultaneous alerts to all emergency contacts
- **Google Maps Integration** - Direct links to accident location
- **Real-time Status Updates** - Live emergency dashboard monitoring

### 🎨 Color-Coded Notification System
- **🔴 Red (Emergency)** - Emergency system activation with pulsing animation
- **🟢 Green (Success)** - Successful email delivery and system completion
- **🟠 Orange (Warning)** - Important alerts and countdown notifications
- **🔴 Red (Error)** - System errors with shake animation for attention
- **🔵 Blue (Info)** - General system information and status updates

### 📧 Emergency Contact Configuration
Current emergency recipients:
- **Primary Contact**: vaibhavmevada796@gmail.com
- **Test Contact**: cipaha2099@gxuzi.com  
- **Emergency Contact**: paresh07suva@gmail.com
- **AMTS Helplines**: emergency@amts.gov.in, control.room@amts.gov.in

### 🧪 Testing Emergency System
1. Navigate to bus route search page
2. Click "Live Track" on any bus route
3. Click "🚨 Simulate Accident" button in tracking modal
4. Confirm emergency alert activation
5. Check configured Gmail addresses for emergency notifications
6. Verify automatic redirect to Emergency Dashboard

## 📧 Bus Pass Email Delivery System

### 🎫 Automated PDF Generation & Delivery
- **Monthly Pass Applications** - Complete form processing with PDF generation
- **Student Pass Applications** - Academic verification with institutional details
- **Automatic Email Delivery** - PDF passes sent directly to applicant email
- **Professional Email Templates** - AMTS-branded communication with usage instructions
- **PDF Attachment Security** - Secure file generation and email delivery

### 📋 Bus Pass Features
- **Personal Information Management** - Complete user profile integration
- **Route-Specific Passes** - Customized for specific bus routes and stops
- **Validity Period Tracking** - Automatic start/end date calculation
- **Student Verification** - School/college details and student ID integration
- **QR Code Integration** - Digital verification for conductors

### 📱 Pass Usage Instructions
- **Mobile-Friendly PDFs** - Optimized for smartphone display
- **Conductor Verification** - Show PDF to bus conductor when boarding
- **Backup Recommendations** - Keep digital and physical copies
- **Customer Support** - Direct contact information for pass-related issues

## 🛠️ Technology Stack & Architecture

### Backend Technologies
- **Django 5.2.10** - Python web framework with advanced ORM
- **SQLite Database** - Development database with easy migration to PostgreSQL
- **Gmail SMTP Integration** - Real email delivery with App Password authentication
- **ReportLab PDF Generation** - Professional PDF creation for bus passes
- **QR Code Library** - Digital ticket and pass verification

### Frontend Technologies  
- **Responsive HTML5/CSS3** - Mobile-first design approach
- **Bootstrap Framework** - Professional UI components and grid system
- **JavaScript ES6+** - Modern client-side functionality and AJAX
- **Leaflet Maps** - Interactive GPS tracking and location services
- **Real-time Notifications** - Color-coded system status updates

### Security & Performance
- **CSRF Protection** - Cross-site request forgery prevention
- **Environment Variables** - Secure configuration management
- **Session Management** - User authentication and authorization
- **Email Rate Limiting** - Gmail SMTP compliance and delivery optimization

## 📱 Application URLs & Navigation

### 🏠 Main Application Routes
- **`/`** - Home page with bus search and recent searches
- **`/search/`** - Advanced bus route search with live tracking
- **`/my-bookings/`** - User booking history and ticket management
- **`/login/`** - User authentication and session management
- **`/register/`** - New user registration with form validation

### 🎫 Bus Pass System Routes
- **`/bus-pass/monthly/`** - Monthly pass application form
- **`/bus-pass/student/`** - Student pass application with academic verification
- **`/my-passes/`** - User pass history and PDF downloads

### 🚨 Emergency System Routes
- **`/emergency-dashboard/`** - Emergency management and monitoring
- **`/api/emergency-accident/`** - Emergency notification API endpoint
- **`/api/update-bus-status/`** - Real-time bus status updates

### 🔧 API Endpoints
- **`/api/search-buses/`** - Bus route search and planning
- **`/api/get-active-buses/`** - Live bus tracking data
- **`/api/create-booking/`** - Ticket booking and payment processing
- **`/api/get-nearby-stops/`** - Location-based stop discovery

## 🔒 Security & Configuration

### 🛡️ Security Features
- **Environment Variable Configuration** - Sensitive data protection
- **CSRF Token Protection** - Cross-site request forgery prevention  
- **User Session Management** - Secure authentication and authorization
- **Email Security** - Gmail App Password integration for secure delivery
- **Input Validation** - Form data sanitization and validation
- **Admin Panel Security** - Separate authentication for administrative access

### ⚙️ Configuration Management
- **`.env` File Support** - Environment-specific configuration
- **Django Settings** - Modular configuration with development/production modes
- **Database Configuration** - Easy migration from SQLite to PostgreSQL
- **Email Backend Configuration** - Multiple email delivery options (SMTP, Console, File)

## 🚌 Advanced Bus System Features

### 📍 Real-Time Tracking System
- **Live GPS Coordinates** - Real-time bus location updates
- **Route Visualization** - Interactive maps with bus stops and routes
- **Multi-Bus Tracking** - Track multiple buses on same route
- **Direction Detection** - Forward/reverse journey identification
- **Speed Monitoring** - Real-time speed tracking and status updates

### 🎯 Smart Route Planning
- **Multi-Transfer Routes** - Complex journey planning with bus changes
- **Optimal Route Selection** - Best route recommendations based on time/distance
- **Stop-to-Stop Navigation** - Detailed journey instructions
- **Real-Time Updates** - Live route status and delay notifications

### 🎫 Digital Ticketing System
- **QR Code Generation** - Secure digital ticket verification
- **Mobile-Optimized Tickets** - Smartphone-friendly ticket display
- **Booking History** - Complete transaction and journey records
- **Payment Integration** - Secure online payment processing

## 📊 Emergency Dashboard & Monitoring

### 🚨 Real-Time Emergency Management
- **Active Emergency Monitoring** - Live status of all emergency situations
- **GPS Location Tracking** - Precise accident location with Google Maps integration
- **Email Notification Status** - Real-time delivery confirmation and failure tracking
- **Emergency Response Coordination** - Centralized command center for incident management
- **Multi-Bus Emergency Handling** - Simultaneous emergency management across fleet

### 📈 System Analytics & Reporting
- **Emergency Response Metrics** - Response time and notification delivery statistics
- **Bus Performance Tracking** - Route efficiency and on-time performance
- **User Engagement Analytics** - Booking patterns and system usage statistics
- **Email Delivery Reports** - Comprehensive email system performance monitoring

## 🎯 Future Enhancements & Roadmap

### 📱 Mobile & Communication
- **SMS Notification Integration** - Multi-channel emergency communication
- **Mobile App Development** - Native iOS/Android applications
- **Push Notification System** - Real-time mobile alerts and updates
- **WhatsApp Integration** - Popular messaging platform integration

### 🤖 Advanced Features
- **AI-Powered Route Optimization** - Machine learning for better route planning
- **Predictive Analytics** - Bus delay prediction and passenger flow analysis
- **IoT Integration** - Real sensor data from buses and stops
- **Multi-Language Support** - Gujarati, Hindi, and English language options

### 🌐 System Expansion
- **Multi-City Support** - Expansion to other municipal transport systems
- **Integration APIs** - Third-party service integration capabilities
- **Advanced Reporting Dashboard** - Comprehensive analytics and business intelligence
- **Real-Time Passenger Counting** - Live bus capacity and crowd management

## 🤝 Contributing & Support

### 👨‍💻 Development Team
- **Lead Developer**: AMTS Development Team
- **Emergency System**: Real-time safety notification specialist
- **Email Integration**: Gmail SMTP and PDF delivery expert
- **Frontend Design**: Responsive UI/UX implementation

### 📞 Support & Contact
- **Technical Support**: support@amts.gov.in
- **Emergency Helpline**: +91-79-2658-0000
- **AMTS Control Room**: control.room@amts.gov.in
- **System Administrator**: admin@amts.gov.in

### 🐛 Bug Reports & Feature Requests
- **GitHub Issues**: Use repository issue tracker
- **Email Support**: Include system logs and error details
- **Emergency Issues**: Contact AMTS control room immediately

---

## 🏆 System Highlights

**🚨 Advanced Emergency Safety System** - Real-time accident detection with multi-contact notification  
**📧 Automated Email Delivery** - Professional bus pass PDF delivery with Gmail integration  
**🎨 Color-Coded User Interface** - Intuitive visual feedback system for all operations  
**📱 Mobile-Responsive Design** - Optimized for smartphones and tablets  
**🔒 Enterprise Security** - Production-ready security features and data protection  

---

**Developed for Ahmedabad Municipal Transport Service**  
*Next-generation bus management system with emergency-ready capabilities and automated passenger services*

**Version**: 2.0 | **Last Updated**: January 2026 | **Status**: Production Ready