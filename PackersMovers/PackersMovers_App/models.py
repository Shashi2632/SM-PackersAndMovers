from django.db import models
from django.urls import reverse

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name

class WithinCityBooking(models.Model):
    origin_address = models.CharField(max_length=255)
    destination_address = models.CharField(max_length=255)
    dateofinquiry = models.CharField(max_length=20)  # Storing formatted datetime string directly
    orderbookeddate = models.CharField(max_length=20,default='Not Booked')
    location_city = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    services = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Within City Booking - {self.name} - {self.dateofinquiry}"

    def get_absolute_url(self):
        return reverse('within_city_booking')

class BetweenCitiesBooking(models.Model):
    origin_address_city = models.CharField(max_length=100)
    destination_address_city = models.CharField(max_length=100)
    dateofinquiry = models.CharField(max_length=20)  # Storing formatted datetime string directly
    orderbookeddate = models.CharField(max_length=20,default='Not Booked')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    services = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Between Cities Booking - {self.name} - {self.dateofinquiry}"

    def get_absolute_url(self):
        return reverse('between_cities_booking')

class Service(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Service Name')
    description = models.TextField(verbose_name='Service Description')
    image = models.ImageField(upload_to='service_images/', null=True, blank=True, verbose_name='Service Image')

    def __str__(self):
        return self.name
