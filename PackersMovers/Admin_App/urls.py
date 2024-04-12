from django.urls import path
from Admin_App import views

app_name = 'Admin_App'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('calendar/', views.calendar, name='calendar'),
    path('invoice/', views.invoice, name='invoice'),
    path('emailhtml/', views.emailhtml, name='emailhtml'),
    path('email-inquiry/', views.email_inquiry, name='email-inquiry'),
    path('error/<int:status_code>/', views.error_view, name='error'),
    path('display_bookings/', views.display_bookings, name='display_bookings'),
    path('get_booking/', views.get_booking_details, name='get_booking'),
    path('booking/<int:booking_id>/', views.get_booking_details, name='booking'),
    
]