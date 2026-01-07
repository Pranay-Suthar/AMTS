# 🎫 Bus Pass System Implementation Guide

## ✅ What's Been Done

1. **Model Created** - `BusPass` model added to `models.py`
2. **Installing** - `reportlab` library for PDF generation

## 📋 Next Steps to Complete

### Step 1: Run Migrations

```powershell
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Add Views (Add to `views.py`)

```python
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from django.http import FileResponse
from .models import BusPass
from datetime import datetime, timedelta

@login_required
def bus_pass_form(request, pass_type):
    """Display bus pass application form"""
    return render(request, 'my_amts/bus_pass_form.html', {
        'pass_type': pass_type
    })

@login_required
@csrf_exempt
def submit_bus_pass(request):
    """Handle bus pass form submission and generate PDF"""
    if request.method == 'POST':
        try:
            pass_type = request.POST.get('pass_type')
            
            # Calculate validity dates
            start_date = datetime.now().date()
            if pass_type == 'MONTHLY':
                end_date = start_date + timedelta(days=30)
            else:  # STUDENT
                end_date = start_date + timedelta(days=365)
            
            # Create bus pass record
            bus_pass = BusPass.objects.create(
                user=request.user,
                pass_type=pass_type,
                full_name=request.POST.get('full_name'),
                date_of_birth=request.POST.get('date_of_birth'),
                gender=request.POST.get('gender'),
                phone_number=request.POST.get('phone_number'),
                email=request.POST.get('email'),
                address=request.POST.get('address'),
                from_stop=request.POST.get('from_stop'),
                to_stop=request.POST.get('to_stop'),
                route_number=request.POST.get('route_number'),
                school_college_name=request.POST.get('school_college_name', ''),
                student_id=request.POST.get('student_id', ''),
                class_year=request.POST.get('class_year', ''),
                start_date=start_date,
                end_date=end_date
            )
            
            # Generate PDF
            pdf_path = generate_bus_pass_pdf(bus_pass)
            bus_pass.pdf_file = pdf_path
            bus_pass.save()
            
            return JsonResponse({
                'status': 'success',
                'pass_id': str(bus_pass.pass_id),
                'pdf_url': f'/media/{pdf_path}'
            })
            
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=400)

def generate_bus_pass_pdf(bus_pass):
    """Generate PDF for bus pass"""
    import os
    from django.conf import settings
    
    # Create PDF file path
    filename = f"bus_pass_{bus_pass.pass_id}.pdf"
    filepath = os.path.join(settings.MEDIA_ROOT, 'pass_pdfs', filename)
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    # Create PDF
    c = canvas.Canvas(filepath, pagesize=A4)
    width, height = A4
    
    # Header
    c.setFillColorRGB(0.1, 0.14, 0.49)  # AMTS Blue
    c.rect(0, height - 2*inch, width, 2*inch, fill=True)
    
    c.setFillColorRGB(1, 1, 1)  # White text
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width/2, height - 1*inch, "AHMEDABAD MUNICIPAL")
    c.drawCentredString(width/2, height - 1.4*inch, "TRANSPORT SERVICE (AMTS)")
    
    c.setFont("Helvetica-Bold", 18)
    c.drawCentredString(width/2, height - 1.8*inch, bus_pass.get_pass_type_display().upper())
    
    # Pass Details Box
    y = height - 3*inch
    c.setFillColorRGB(0, 0, 0)
    c.setFont("Helvetica-Bold", 12)
    
    # Personal Information
    c.drawString(1*inch, y, "PERSONAL INFORMATION")
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    
    c.drawString(1*inch, y, f"Pass ID: {bus_pass.pass_id}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Full Name: {bus_pass.full_name}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Date of Birth: {bus_pass.date_of_birth.strftime('%d/%m/%Y')}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Gender: {bus_pass.get_gender_display()}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Phone: {bus_pass.phone_number}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Email: {bus_pass.email}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Address: {bus_pass.address}")
    
    # Route Information
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "ROUTE INFORMATION")
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    
    c.drawString(1*inch, y, f"From: {bus_pass.from_stop}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"To: {bus_pass.to_stop}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Route Number: {bus_pass.route_number}")
    
    # Student Information (if applicable)
    if bus_pass.pass_type == 'STUDENT':
        y -= 0.5*inch
        c.setFont("Helvetica-Bold", 12)
        c.drawString(1*inch, y, "STUDENT INFORMATION")
        y -= 0.3*inch
        c.setFont("Helvetica", 10)
        
        c.drawString(1*inch, y, f"Institution: {bus_pass.school_college_name}")
        y -= 0.25*inch
        c.drawString(1*inch, y, f"Student ID: {bus_pass.student_id}")
        y -= 0.25*inch
        c.drawString(1*inch, y, f"Class/Year: {bus_pass.class_year}")
    
    # Validity
    y -= 0.5*inch
    c.setFont("Helvetica-Bold", 12)
    c.drawString(1*inch, y, "VALIDITY")
    y -= 0.3*inch
    c.setFont("Helvetica", 10)
    
    c.drawString(1*inch, y, f"Valid From: {bus_pass.start_date.strftime('%d/%m/%Y')}")
    y -= 0.25*inch
    c.drawString(1*inch, y, f"Valid Until: {bus_pass.end_date.strftime('%d/%m/%Y')}")
    
    # Footer
    c.setFont("Helvetica-Oblique", 8)
    c.drawCentredString(width/2, 1*inch, "This is a computer-generated pass. No signature required.")
    c.drawCentredString(width/2, 0.7*inch, f"Generated on: {datetime.now().strftime('%d/%m/%Y %I:%M %p')}")
    
    # Border
    c.setStrokeColorRGB(0.1, 0.14, 0.49)
    c.setLineWidth(2)
    c.rect(0.5*inch, 0.5*inch, width - 1*inch, height - 1*inch)
    
    c.save()
    
    return f"pass_pdfs/{filename}"

@login_required
def my_passes(request):
    """View all user's bus passes"""
    passes = BusPass.objects.filter(user=request.user)
    return render(request, 'my_amts/my_passes.html', {'passes': passes})
```

### Step 3: Add URLs (Add to `urls.py`)

```python
path('bus-pass/<str:pass_type>/', views.bus_pass_form, name='bus_pass_form'),
path('api/submit-bus-pass/', views.submit_bus_pass, name='submit_bus_pass'),
path('my-passes/', views.my_passes, name='my_passes'),
```

### Step 4: Create Template (`bus_pass_form.html`)

Create file: `templates/my_amts/bus_pass_form.html`

This template will contain the AMTS-style bus pass application form with all fields.

### Step 5: Update Navigation

Add "Services" menu to `base.html` navigation with links to Monthly Pass and Student Pass.

## 🎯 Features

✅ Monthly Pass Application
✅ Student Pass Application  
✅ AMTS-style PDF generation
✅ Auto-calculated validity dates
✅ Personal information capture
✅ Route details
✅ Student-specific fields
✅ PDF download
✅ Pass history

## 📄 PDF Contains

- AMTS Header (Blue)
- Pass Type (Monthly/Student)
- Pass ID
- Personal Information
- Route Details
- Student Information (if applicable)
- Validity Dates
- Generation Timestamp
- Professional Border

## 🚀 Ready to Implement!

Run the migrations and I'll create the complete template files!
