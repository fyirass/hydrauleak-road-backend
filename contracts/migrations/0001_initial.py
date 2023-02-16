# Generated by Django 3.2.16 on 2023-02-16 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
        ('maps', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_title', models.CharField(blank=True, max_length=150)),
                ('contract_description', models.TextField(blank=True)),
                ('contract_type', models.CharField(blank=True, choices=[('Hight', 'Hight'), ('Simple', 'Simple'), ('PipeSearch', 'Pipesearch')], default='Simple', max_length=50)),
                ('contract_status', models.CharField(blank=True, choices=[('NotStart', 'Notstart'), ('Pending', 'Pending'), ('expired', 'Completed')], default='NotStart', max_length=50)),
                ('contract_work_type', models.CharField(blank=True, choices=[('Fire Hydrant Inspection', 'Fire Hydrant Inspection'), ('All City Inspections', 'All City Inspections'), ('Clarifying the location of the leak', 'Clarify Leak Location'), ('Solve high consumption problem but the leak is not identified', 'Solve High Consumption')], default='Fire Hydrant Inspection', max_length=200)),
                ('contract_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('contract_estimate_end_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=15)),
                ('is_published', models.CharField(choices=[('Published', 'Is Published'), ('Not Published', 'Is Not Published')], default='Not Published', max_length=50)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='clients.client')),
                ('zone', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maps.zone')),
            ],
        ),
    ]
