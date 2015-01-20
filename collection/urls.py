from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.sitemaps.views import sitemap
from photologue.sitemaps import GallerySitemap, PhotoSitemap


sitemaps = {
    'photologue_galleries': GallerySitemap,
    'photologue_photos': PhotoSitemap,
    }


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^photologue/', include('photologue.urls', namespace='photologue')),
    url(r'^$', TemplateView.as_view(template_name="homepage.html"), name='homepage'),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
