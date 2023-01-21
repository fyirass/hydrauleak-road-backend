# Generated by Django 3.2.16 on 2023-01-21 01:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20230121_0139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='map',
            name='leaker_vehicles',
        ),
        migrations.RemoveField(
            model_name='map',
            name='pipes',
        ),
        migrations.RemoveField(
            model_name='map',
            name='sensors',
        ),
        migrations.RemoveField(
            model_name='map',
            name='zones',
        ),
        migrations.AddField(
            model_name='leakervehicle',
            name='map',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='map',
            name='leakervehicle_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='map',
            name='pipe_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='map',
            name='sensor_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='map',
            name='zone_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pipe',
            name='map',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pipeacces',
            name='map',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sensor',
            name='map',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zone',
            name='map',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maps.map'),
            preserve_default=False,
        ),
    ]
