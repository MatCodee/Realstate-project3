# Esta es la configuracion del sitemap:

from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Blog

class StaticSitemap(Sitemap):
    """Reverse 'static' views for XML sitemap."""
    changefreq = "daily"
    priority = 0.5

    def items(self):
        # Return list of url names for views to include in sitemap
        return ['home','about','services','contact','team','properties']

    def location(self, item):
        return reverse(item)

class DynamicSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Blog.objects.all()