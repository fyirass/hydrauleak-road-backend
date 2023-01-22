# Generated by Django 3.2.16 on 2023-01-22 03:10

import datetime
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
            name='ClienTFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Client_file', models.FileField(blank=True, upload_to='Client_files/')),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('inscription_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('client_files', models.ManyToManyField(blank=True, to='clients.ClienTFile')),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
