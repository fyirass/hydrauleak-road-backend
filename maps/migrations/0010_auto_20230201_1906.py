# Generated by Django 3.2.16 on 2023-02-01 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0009_auto_20230201_1905'),
    ]

    operations = [
        migrations.RenameField(
            model_name='zone',
            old_name='sensor_description',
            new_name='zone_description',
        ),
        migrations.RenameField(
            model_name='zone',
            old_name='sensor_title',
            new_name='zone_title',
        ),
    ]
