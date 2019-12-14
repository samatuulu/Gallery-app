from audioop import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from webapp.models import Gallery


class IndexView(ListView):
    model = Gallery
    template_name = 'index.html'
    context_object_name = 'gallery'

    def get_queryset(self):
        return Gallery.objects.all()


class GalleryDetailView(DetailView):
    template_name = 'detail.html'
    model = Gallery
    context_object_name = 'gallery'


class GalleryCreateView(CreateView):
    model = Gallery
    template_name = 'create.html'
    fields = ('photo', 'signature', 'amount_of_likes', 'author')

    def get_success_url(self):
        return reverse_lazy('webapp:index')


class GalleryUpdateView(UpdateView):
    model = Gallery
    template_name = 'update.html'
    fields = ('photo', 'signature', 'amount_of_likes', 'author')
    context_object_name = 'gallery'

    def get_success_url(self):
        return reverse_lazy('webapp:index')