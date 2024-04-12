from django.shortcuts import render
from django.urls import reverse
from .models import Service

def home(request):
    services = Service.objects.all()
    canonical_url = request.build_absolute_uri(reverse('home'))  # Example URL, replace with your actual canonical URL
    context = {'services': services, 'canonical_url': canonical_url}
    return render(request, 'home_page.html', context)

def about(request):
    canonical_url = request.build_absolute_uri(reverse('about'))  # Example URL, replace with your actual canonical URL
    context = {'canonical_url': canonical_url}
    return render(request, 'about.html', context)

def contact(request):
    canonical_url = request.build_absolute_uri(reverse('contact-us'))  # Example URL, replace with your actual canonical URL
    context = {'canonical_url': canonical_url}
    return render(request, 'contact.html', context)

def services(request):
    services = Service.objects.all()
    canonical_url = request.build_absolute_uri(reverse('services'))  # Example URL, replace with your actual canonical URL
    context = {'services': services, 'canonical_url': canonical_url}
    return render(request, 'services.html', context)

def thank_you(request):
    canonical_url = request.build_absolute_uri(reverse('thank_you'))  # Example URL, replace with your actual canonical URL
    context = {'canonical_url': canonical_url}
    return render(request, 'thank_you.html', context)
