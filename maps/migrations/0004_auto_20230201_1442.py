# Generated by Django 3.2.16 on 2023-02-01 13:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_zone_zone_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='zone_color',
            field=models.CharField(choices=[('green', 'Green'), ('orange', 'Orange'), ('red', 'Red')], default='orange', max_length=20),
        ),
        migrations.AlterField(
            model_name='zone',
            name='zone_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='zone',
            name='zone_status',
            field=models.CharField(choices=[('notStart', 'Not Started'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='notStart', max_length=20),
        ),
    ]
