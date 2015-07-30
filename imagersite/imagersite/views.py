from django.views.generic import TemplateView
from photo.models import Photos

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        try:
            context["photo"] = Photos.objects.filter(published='public')\
                .order_by('?').first()
            # returns pic of dog if above is context is false/att error
        except AttributeError:
            context["photo"] = 'imagersite/media/photo_files/15-07-28/dog.jpg'
        return context

