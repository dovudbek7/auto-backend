from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['auto:home', 'auto:about', 'auto:contact', 'auto:quote','auto:gallery','auto:services']

    def location(self, item):
        return reverse(item)