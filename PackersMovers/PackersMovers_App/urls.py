from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, about, services, contact, thank_you
from .form_views import contact_view, within_city_booking_view, between_cities_booking_view, update_inquiry

from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact-us/', contact, name='contact-us'),
    path('services/', services, name='services'),
    path('contact/', contact_view, name='contact'),
    path('thank_you/', thank_you, name='thank_you'),
    path('within_city_booking/', within_city_booking_view, name='within_city_booking'),
    path('between_cities_booking/', between_cities_booking_view, name='between_cities_booking'),
    path('update-inquiry/', update_inquiry, name='update_inquiry'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
