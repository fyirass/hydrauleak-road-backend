# Generated by Django 3.2.16 on 2023-02-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_alter_zone_zone_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='sensor_description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='zone',
            name='sensor_title',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
