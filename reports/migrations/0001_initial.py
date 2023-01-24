# Generated by Django 3.2.16 on 2023-01-23 21:41

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leakers', '0001_initial'),
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('add_sensor_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('add_mark_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('add_pipe_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('add_pipe_access_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('image', models.ImageField(blank=True, upload_to='report_image')),
                ('report_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clients.client')),
                ('leaker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leakers.leaker')),
            ],
        ),
    ]
