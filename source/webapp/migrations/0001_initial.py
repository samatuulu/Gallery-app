# Generated by Django 2.2 on 2019-12-14 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='uploads', verbose_name='Photo')),
                ('signature', models.CharField(max_length=200, verbose_name='Signature')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('amount_of_likes', models.IntegerField(default=0, verbose_name='Like')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='UserPostLikes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Gallery')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('comment_photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.Gallery')),
                ('commnent_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
