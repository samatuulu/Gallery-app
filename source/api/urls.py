from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import CommentViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]