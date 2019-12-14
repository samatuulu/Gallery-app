from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.models import Gallery, Comments


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'registration/login.html', context=context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('webapp:index')


class IndexView(ListView):
    model = Gallery
    template_name = 'index.html'
    context_object_name = 'gallery'

    def get_queryset(self):
        return Gallery.objects.order_by('-created_at')


class GalleryDetailView(DetailView):
    template_name = 'detail.html'
    model = Gallery
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        context = super().get_context_data(**kwargs)
        photo = pk
        comments = Comments.objects.filter(comment_photo=photo)
        context['comments'] = comments
        return context


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


class GalleryDeleteView(DeleteView):
    model = Gallery
    template_name = 'delete.html'
    success_url = reverse_lazy('webapp:index')
    context_object_name = 'gallery'

    def delete(self, request, *args, **kwargs):
        gallery = self.object = self.get_object()
        gallery.delete()
        return HttpResponseRedirect(self.get_success_url())