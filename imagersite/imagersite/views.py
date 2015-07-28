from django.views.generic import TemplateView
from photo.models import Photo


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["photo"] = Photo.objects.filter(published='public')\
            .order_by('?').first()
        return context
