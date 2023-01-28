# Generated by Django 3.2.16 on 2023-01-28 21:05

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_rename_zone_coordinates_pipe_pipe_coordinates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pipe',
            name='pipe_coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='zone',
            name='zone_coordinates',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), size=None), size=None),
        ),
    ]
