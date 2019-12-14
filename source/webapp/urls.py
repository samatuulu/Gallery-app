from django.urls import path
from webapp.views import IndexView, GalleryDetailView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('gallery/<int:pk>/detail', GalleryDetailView.as_view(), name='detail'),
]