# my_amts/models.py

from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw
from django.conf import settings
import os
import uuid
from django.utils import timezone
from datetime import datetime, time
from django.contrib.auth.models import User

class Bus(models.Model):
    bus_number = models.CharField(max_length=10, unique=True)
    stops = models.JSONField()

    def __str__(self):
        return self.bus_number

    def get_stop_names(self):
        return [stop['name'] for stop in self.stops]

    class Meta:
        verbose_name_plural = "Buses"

class ActiveBus(models.Model):
    bus = models.ForeignKey(
        Bus, 
        on_delete=models.CASCADE, 
        related_name='active_instances'
    )
    identifier = models.CharField(
        max_length=20,
        unique=True,
        help_text="Unique identifier for active bus (e.g., '45-1', '45-2')"
    )
    current_location = models.CharField(
        max_length=100,
        help_text="Current stop or location of the bus"
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('ON_TIME', 'On Time'),
            ('DELAYED', 'Delayed'),
            ('OUT_OF_SERVICE', 'Out of Service')
        ],
        default='ON_TIME'
    )
    last_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    # Safety Feature Fields
    speed = models.FloatField(default=35.0, help_text="Current speed in km/h")
    is_manual_stop = models.BooleanField(default=False, help_text="True if driver manually stopped bus")
    is_accident = models.BooleanField(default=False, help_text="True if accident/breakdown detected")
    latitude = models.FloatField(null=True, blank=True, help_text="Current latitude position")
    longitude = models.FloatField(null=True, blank=True, help_text="Current longitude position")

    def __str__(self):
        return f"{self.identifier} - {self.current_location}"

    class Meta:
        verbose_name = "Active Bus"
        verbose_name_plural = "Active Buses"
        ordering = ['identifier']

class Booking(models.Model):
    booking_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    bus_number = models.CharField(max_length=10)
    from_stop = models.CharField(max_length=100)
    to_stop = models.CharField(max_length=100)
    booking_date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, default='COMPLETED')

    def __str__(self):
        return f"Booking {self.booking_id}"

    class Meta:
        db_table = 'my_amts_booking'

class Ticket(models.Model):
    ticket_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, related_name='tickets')
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def generate_qr_code(self):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"Ticket ID: {self.ticket_id}\n"
                   f"Bus: {self.booking.bus_number}\nFrom: {self.booking.from_stop}\n"
                   f"To: {self.booking.to_stop}\n"
                   f'Valid until : {self.booking.booking_date}')
        qr.make(fit=True)

        qr_image = qr.make_image(fill_color="black", back_color="white")
        stream = BytesIO()
        qr_image.save(stream, 'PNG')
        filename = f'qr_code_{self.ticket_id}.png'
        self.qr_code.save(filename, File(stream), save=False)

    def save(self, *args, **kwargs):
        if not self.qr_code:
            self.generate_qr_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Ticket {self.ticket_id}"

    class Meta:
        db_table = 'my_amts_ticket'

class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    from_stop = models.CharField(max_length=100)
    to_stop = models.CharField(max_length=100)
    search_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-search_time']  # Most recent first
        verbose_name_plural = "Search histories"

    def __str__(self):
        return f"{self.user.username}: {self.from_stop} to {self.to_stop}"

class BusPass(models.Model):
    PASS_TYPES = [
        ('MONTHLY', 'Monthly Pass'),
        ('STUDENT', 'Student Pass'),
    ]
    
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    
    pass_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pass_type = models.CharField(max_length=10, choices=PASS_TYPES)
    
    # Personal Information
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    
    # Pass Details
    from_stop = models.CharField(max_length=100)
    to_stop = models.CharField(max_length=100)
    route_number = models.CharField(max_length=10)
    
    # Student-specific fields
    school_college_name = models.CharField(max_length=200, blank=True, null=True)
    student_id = models.CharField(max_length=50, blank=True, null=True)
    class_year = models.CharField(max_length=50, blank=True, null=True)
    
    # Documents
    photo = models.ImageField(upload_to='pass_photos/', blank=True, null=True)
    id_proof = models.FileField(upload_to='pass_documents/', blank=True, null=True)
    student_id_card = models.FileField(upload_to='pass_documents/', blank=True, null=True)
    
    # Pass validity
    start_date = models.DateField()
    end_date = models.DateField()
    
    # Status
    application_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    pdf_file = models.FileField(upload_to='pass_pdfs/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.get_pass_type_display()} - {self.full_name}"
    
    class Meta:
        verbose_name = "Bus Pass"
        verbose_name_plural = "Bus Passes"
        ordering = ['-application_date']