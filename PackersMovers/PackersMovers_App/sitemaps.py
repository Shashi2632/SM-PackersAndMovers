from django.contrib.sitemaps.views import sitemap
from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from .models import Service

class StaticViewSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ['home', 'about', 'contact-us', 'services']

    def location(self, item):
        return reverse(item)
