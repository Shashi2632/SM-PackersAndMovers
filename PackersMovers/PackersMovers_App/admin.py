from django.contrib import admin
from .models import Contact, WithinCityBooking, BetweenCitiesBooking, Service

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')
    search_fields = ('name', 'email', 'phone')

@admin.register(WithinCityBooking)
class WithinCityBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateofinquiry', 'location_city', 'email', 'phone', 'origin_address', 'destination_address', 'status', 'orderbookeddate')
    search_fields = ('name', 'location_city', 'email', 'phone', 'dateofinquiry', 'orderbookeddate')

@admin.register(BetweenCitiesBooking)
class BetweenCitiesBookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'dateofinquiry', 'orderbookeddate', 'email', 'phone', 'origin_address_city','destination_address_city', 'status')
    search_fields = ('name', 'email', 'phone', 'dateofinquiry', 'orderbookeddate')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
