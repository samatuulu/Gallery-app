from django.views.generic import TemplateView, ListView

from webapp.models import Gallery


class IndexView(ListView):
    model = Gallery
    template_name = 'index.html'
    context_object_name = 'gallery'

    def get_queryset(self):
        return Gallery.objects.all()