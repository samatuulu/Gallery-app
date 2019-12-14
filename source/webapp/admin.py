from django.contrib import admin
from .models import Gallery, Comments, UserPostLikes

admin.site.register(Gallery)
admin.site.register(Comments)
admin.site.register(UserPostLikes)
