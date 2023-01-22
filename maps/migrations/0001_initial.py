# Generated by Django 3.2.16 on 2023-01-22 03:11

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('leakers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('map_title', models.CharField(max_length=100)),
                ('map_description', models.TextField()),
                ('map_creation_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Pipe',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pipe_status', models.CharField(choices=[('good', 'Good'), ('unknown', 'Unknown'), ('critical', 'Critical')], default='unknown', max_length=20)),
                ('pipe_description', models.TextField()),
                ('pipe_creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('pipe_type', models.CharField(max_length=50)),
                ('pipe_title', models.CharField(max_length=100)),
                ('pipe_length', models.FloatField()),
                ('pipe_material', models.CharField(max_length=50)),
                ('pipe_diameter', models.FloatField()),
                ('pipe_access_number', models.IntegerField(blank=True, default=0)),
                ('pipe_mark_number', models.IntegerField(blank=True, default=0)),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.map')),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_num', models.IntegerField(default=0)),
                ('zone_date', models.DateTimeField()),
                ('zone_status', models.CharField(choices=[('notStart', 'Not Started'), ('Pending', 'Pending'), ('Completed', 'Completed')], max_length=20)),
                ('zone_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=list, size=200)),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='maps', to='maps.map')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('sensor_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('sensor_creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('sensor_photo', models.ImageField(blank=True, upload_to='sensor')),
                ('sensor_type', models.CharField(max_length=50)),
                ('sensor_title', models.CharField(max_length=100)),
                ('sensor_description', models.TextField()),
                ('sensor_frequency', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=None), blank=True, size=2)),
                ('sensor_Indication', models.CharField(choices=[('critical', 'Critical'), ('notable', 'Notable'), ('good', 'Good'), ('unknown', 'Unknown'), ('empty', 'Empty')], default='unknown', max_length=20)),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.map')),
            ],
        ),
        migrations.CreateModel(
            name='PipeAcces',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pipe_access_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('pipe_access_title', models.CharField(max_length=100)),
                ('pipe_access_description', models.TextField()),
                ('pipe_access_type', models.CharField(choices=[('HouseValve', 'House Valve'), ('FirePole', 'Fire Pole'), ('FireHydrantValve', 'Fire Hydrant Valve'), ('Other', 'Other')], default='other', max_length=20)),
                ('pipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipe_accesses', to='maps.pipe')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mark_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('mark_creation_date', models.DateTimeField(default=datetime.datetime.now)),
                ('mark_photo', models.ImageField(blank=True, upload_to='marks')),
                ('mark_description', models.TextField()),
                ('pipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pipe_marks', to='maps.pipe')),
            ],
        ),
        migrations.CreateModel(
            name='LeakerVehicle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('leaker_coordinates', django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), size=2)),
                ('leaker_vehicle_title', models.CharField(max_length=100)),
                ('leaker_vehicle_description', models.TextField()),
                ('leaker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='leakers.leaker')),
                ('map', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.map')),
            ],
        ),
    ]
