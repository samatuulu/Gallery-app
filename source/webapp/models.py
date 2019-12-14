from django.contrib.auth.models import User
from django.db import models


class Gallery(models.Model):
    photo = models.ImageField(upload_to='uploads', null=False, blank=False, verbose_name='Photo')
    signature = models.CharField(max_length=200, null=False, blank=False, verbose_name='Signature')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    amount_of_likes = models.IntegerField(default=0, verbose_name='Like')
    author = models.ForeignKey(User, related_name='gallery_user', verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return self.signature

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'


class Comments(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False)
    comment_photo = models.ForeignKey('webapp.Gallery', null=False, blank=False, on_delete=models.CASCADE)
    commnent_author = models.ForeignKey(User, related_name='comment_user', verbose_name='User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    def __str__(self):
        return str(self.commnent_author)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'


class UserPostLikes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    like = models.IntegerField(default=0, verbose_name='Like')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + ':' + str(self.gallery)