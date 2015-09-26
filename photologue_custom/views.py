from photologue.views import GalleryListView
from photologue.views import PhotoListView, PhotoDetailView, GalleryListView, GalleryDetailView
from photologue.models import Gallery

class NavGalleryListView(GalleryListView):

    def get_context_data(self, **kwargs):
        context = super(NavGalleryListView, self).get_context_data(**kwargs)
        context['nav_galleries'] = Gallery.objects.all()
        return context

class NavPhotoListView(PhotoListView):

    def get_context_data(self, **kwargs):
        context = super(NavPhotoListView, self).get_context_data(**kwargs)
        context['nav_galleries'] = Gallery.objects.all()
        return context

class NavGalleryDetailView(GalleryDetailView):

    def get_context_data(self, **kwargs):
        context = super(NavGalleryDetailView, self).get_context_data(**kwargs)
        context['nav_galleries'] = Gallery.objects.all()
        return context

class NavPhotoDetailView(PhotoDetailView):

    def get_context_data(self, **kwargs):
        context = super(NavPhotoDetailView, self).get_context_data(**kwargs)
        context['nav_galleries'] = Gallery.objects.all()
        return context
