from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^gallerylist/$',
            NavGalleryListView.as_view(),
            name='photologue_custom-gallery-list'),
        url(r'^photolist/$',
            NavPhotoListView.as_view(),
            name='photologue_custom-photo-list'),
        url(r'^gallery/(?P<slug>[\-\d\w]+)/$',
            NavGalleryDetailView.as_view(),
            name='photologue_custom-pl-gallery'),
        url(r'^photo/(?P<slug>[\-\d\w]+)/$',
            NavPhotoDetailView.as_view(),
            name='photologue_custom-pl-photo'),
        ]
