from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from api.serializers import CommentSerializers
from webapp.models import Comments


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comments.objects.all()
    serializer_class = CommentSerializers

    def get_permissions(self):
        if self.action not in ['update', 'partial_update', 'destroy']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        like = self.get_object()
        like.like += 1
        like.save()
        return Response({'id': like.pk, 'rating': like.like})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        like = self.get_object()
        like.like -= 1
        like.save()
        return Response({'id': like.pk, 'rating': like.like})