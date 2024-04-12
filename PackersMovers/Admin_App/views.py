from django.shortcuts import render,get_object_or_404
from PackersMovers_App.models import WithinCityBooking, BetweenCitiesBooking
from django.http import JsonResponse

def dashboard(request):
    return render(request, 'Admin_App/index.html')


def calendar(request):
    return render(request, 'Admin_App/calendar.html')

def invoice(request):
    return render(request, 'Admin_App/invoice.html')
    

def emailhtml(request):
    return render(request, 'Admin_App/thankyou-email.html')

def email_inquiry(request):
    pass
    return render(request, 'Admin_App/inquiry-email.html')

def error_view(request, status_code):
    template_name = None

    if status_code == 400:
        template_name = 'Admin_App/400.html'
    elif status_code == 403:
        template_name = 'Admin_App/403.html'
    elif status_code == 404:
        template_name = 'Admin_App/404.html'
    elif status_code == 500:
        template_name = 'Admin_App/500.html'
    elif status_code == 503:
        template_name = 'Admin_App/503.html'
    # else:
    #     template_name = 'Admin_App/error_generic.html'

    return render(request, template_name, status=status_code)

def display_bookings(request):
    booking_type = request.GET.get('booking','')  # Retrieve the 'booking' query parameter
    

    if booking_type == 'within':
        bookings = WithinCityBooking.objects.all()
        print("bookings_data: ",bookings)
        template_name = 'Admin_App/datatable1.html'
    elif booking_type == 'between':
        bookings = BetweenCitiesBooking.objects.all()
        template_name = 'Admin_App/datatable2.html'
    else:
        # Default to an empty queryset and a default template if 'booking' is neither 'within' nor 'between'
        bookings = []
        template_name = 'Admin_App/datatable.html'

    

    context = {
        'bookings': bookings,
        
    }

    return render(request, template_name, context)

def get_booking_details(request):
    specific_booking_id = request.GET.get('specific_booking_id', None)
    
    specific_booking = None

    if specific_booking_id:
        specific_booking = get_object_or_404(WithinCityBooking, pk=specific_booking_id)

    # Create a dictionary with the relevant data
    data = {
        'specific_booking': {
            'id': specific_booking.id if specific_booking else None,
            'origin_address': specific_booking.origin_address if specific_booking else None,
            'destination_address': specific_booking.destination_address if specific_booking else None,
            'inquirydate': specific_booking.dateofinquiry if specific_booking and specific_booking.dateofinquiry else None,
            'bookeddate': specific_booking.orderbookeddate if specific_booking and specific_booking.orderbookeddate else None,
            'location_city': specific_booking.location_city if specific_booking else None,
            'name': specific_booking.name if specific_booking else None,
            'email': specific_booking.email if specific_booking else None,
            'phone': specific_booking.phone if specific_booking else None,
            'services': specific_booking.services if specific_booking else None,
            'status': specific_booking.status if specific_booking else None,
        },
    }
    
    # Return a JsonResponse with the data
    return JsonResponse(data)
