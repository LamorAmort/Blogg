# Generated by Django 3.2.16 on 2022-12-12 09:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myApp', '0026_profile_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='retweet',
            field=models.ManyToManyField(related_name='retweet', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
