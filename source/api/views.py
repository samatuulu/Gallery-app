from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})