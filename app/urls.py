from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.urls import re_path
from django.contrib.sitemaps.views import sitemap


from .sitemap_conf import StaticSitemap, DynamicSitemap
sitemaps = {'static': StaticSitemap, 'dynamic': DynamicSitemap }

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('real_state.urls')),
    path('blog/',include('blog.urls')),
    
    re_path(r'^robots\.txt$', TemplateView.as_view(template_name='app/robots.txt', content_type='text/plain')),
    re_path(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
