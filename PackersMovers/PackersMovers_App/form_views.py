from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Contact, WithinCityBooking, BetweenCitiesBooking
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from smtplib import SMTPException
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from .email_notifications import send_email_notification

@csrf_exempt
@require_POST
def within_city_booking_view(request):
    if request.method == 'POST':
        # Fetch form data from the request using request.POST
        origin_address = request.POST.get('origin_address')
        destination_address = request.POST.get('destination_address')
        datetime_str = request.POST.get('date')
        location_city = request.POST.get('location_city').title()
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('selected_service')
        print("service: ",service)
        # Convert the datetime string to a formatted datetime string
        formatted_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M').strftime('%d %b %Y %I:%M %p')

        # Create a dictionary with the form data
        form_data = {
            'origin_address': origin_address,
            'destination_address': destination_address,
            'dateofinquiry': formatted_datetime,  # Store formatted datetime string
            'location_city': location_city,
            'name': name,
            'email': email,
            'phone': phone,
            'services': service,
        }

        # Save the within-city booking details to the database
        within_city_booking = WithinCityBooking(**form_data)
        within_city_booking.save()

        # Send email notification
        send_email_notification(form_data)

        # Redirect to a thank_you page
        return HttpResponseRedirect('/thank_you/')

    return render(request, 'index.html')


@csrf_exempt
@require_POST
def between_cities_booking_view(request):
    if request.method == 'POST':
        # Fetch form data from the request using request.POST
        origin_address_city = request.POST.get('origin_address_city').title()
        destination_address_city = request.POST.get('destination_address_city').title()
        datetime_str = request.POST.get('date')
        name = request.POST.get('name').title()
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        service = request.POST.get('selected_service')

        # Convert the datetime string to a formatted datetime string
        formatted_datetime = datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M').strftime('%d %b %Y %I:%M %p')
        # Create a dictionary with the form data
        form_data = {
            'origin_address_city': origin_address_city,
            'destination_address_city': destination_address_city,
            'dateofinquiry': formatted_datetime,
            'name': name,
            'email': email,
            'phone': phone,
            'services': service,
        }

        # Save the between-cities booking details to the database
        between_cities_booking = BetweenCitiesBooking(**form_data)
        between_cities_booking.save()

        # Send email notification
        send_email_notification(form_data)

        # Redirect to a thank_you page
        return HttpResponseRedirect('/thank_you/')

    return render(request, 'index.html')


@csrf_exempt
@require_POST
def contact_view(request):
    if request.method == 'POST':
        # Fetch form data from the request using request.POST
        name = request.POST.get('name').title() 
        email = request.POST.get('email')
        phone_number = request.POST.get('phonenumber')
        message = request.POST.get('message')

        # Create a dictionary with the form data
        form_data = {
            'name': name,
            'email': email,
            'phone': phone_number,
            'message': message,
        }

        # Save the contact details to the database
        contact = Contact(**form_data)
        contact.save()

        # Send email notification
        send_email_notification(form_data)

        # Redirect to a thank_you page
        return HttpResponseRedirect('/thank_you/')

    # Replace with the actual template file path
    return render(request, 'contact.html')


@csrf_exempt
@require_POST
def update_inquiry(request):
    if request.method == 'POST':
        # Get the form data from the request
        id = request.POST.get('inquiryid')
        status = request.POST.get('statusValue')
        bookeddate = request.POST.get('bookeddate')
        print(id)
        print(status)
        print(bookeddate)
        # Convert the datetime string to a formatted datetime string
        formatted_datetime = datetime.strptime(bookeddate, '%Y-%m-%dT%H:%M').strftime('%d %b %Y %I:%M %p')

        # Update the WithinCityBooking object
        within_city_booking = WithinCityBooking.objects.get(pk=id)
        within_city_booking.status = status
        within_city_booking.orderbookeddate = formatted_datetime
        within_city_booking.save()

        # Redirect to the display_bookings URL with query parameter booking=within
        return redirect(reverse('Admin_App:display_bookings') + '?booking=within')

    # Handle GET requests or other cases where method is not POST
    return redirect(reverse('Admin_App:display_bookings') + '?booking=within')
