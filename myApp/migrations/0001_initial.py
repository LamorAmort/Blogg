# Generated by Django 3.2.16 on 2022-11-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=50)),
                ('kisaBilgi', models.CharField(max_length=100)),
                ('resim', models.FileField(upload_to='posts/')),
                ('tarih', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
            ],
        ),
    ]