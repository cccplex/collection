from django.views.generic.base import TemplateView

from photologue.models import Gallery

class NavView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(NavView, self).get_context_data(**kwargs)
        context['nav_galleries'] = Gallery.objects.all()
        return context
