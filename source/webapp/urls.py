from django.urls import path
from webapp.views import IndexView, GalleryDetailView, GalleryCreateView, GalleryUpdateView, GalleryDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('gallery/<int:pk>/detail', GalleryDetailView.as_view(), name='detail'),
    path('gallery/create/', GalleryCreateView.as_view(), name='create'),
    path('gallery/<int:pk>update/', GalleryUpdateView.as_view(), name='update'),
    path('gallery/<int:pk>delete/', GalleryDeleteView.as_view(), name='delete'),
]