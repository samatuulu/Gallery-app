from rest_framework.serializers import ModelSerializer
from webapp.models import Comments


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'text', 'commnent_author', 'created_at']