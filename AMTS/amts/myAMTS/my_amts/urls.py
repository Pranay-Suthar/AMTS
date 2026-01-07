# my_amts/urls.py
from django.urls import path, include
from . import views
from . import ticket_views

urlpatterns = [
    path('', views.home, name='home'),  # This will be the landing page
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('search/', views.search_view, name='search'),
    path('api/search/', views.search_buses, name='search_buses'),
    path('api/buses/<str:bus_number>/active/', views.get_active_buses, name='active_buses'),
    path('api/update-bus-status/', views.update_bus_status, name='update_bus_status'),
    path('book-ticket/', ticket_views.book_ticket, name='book_ticket'),
    path('tickets/', ticket_views.ticket_list, name='ticket_list'),
    path('ticket/<uuid:ticket_id>/', ticket_views.ticket_detail, name='ticket_detail'),
    path('verify-ticket/<uuid:ticket_id>/', ticket_views.verify_ticket, name='verify_ticket'),
    path('api/create-booking/', views.create_booking, name='create_booking'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('api/nearby-stops/', views.get_nearby_stops, name='nearby_stops'),
    path('bus-details/', views.bus_details, name='bus_details'),
    path('available-buses/', views.get_available_buses, name='available_buses'),
    path('api/notify-accident-passengers/', views.notify_accident_passengers, name='notify_accident_passengers'),
    path('api/emergency-accident/', views.emergency_accident_alert, name='emergency_accident_alert'),
    path('emergency-dashboard/', views.emergency_dashboard, name='emergency_dashboard'),
    path('bus-pass/monthly/', views.monthly_pass_form, name='monthly_pass'),
    path('bus-pass/student/', views.student_pass_form, name='student_pass'),
    path('api/submit-bus-pass/', views.submit_bus_pass, name='submit_bus_pass'),
    path('my-passes/', views.my_passes, name='my_passes'),
]