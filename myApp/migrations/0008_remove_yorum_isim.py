# Generated by Django 3.2.16 on 2022-11-20 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_yorum_kullanici'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yorum',
            name='isim',
        ),
    ]
