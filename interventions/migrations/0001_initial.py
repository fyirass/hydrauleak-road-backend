# Generated by Django 3.2.16 on 2023-04-10 13:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intervention_title', models.CharField(max_length=150)),
                ('intervention_description', models.TextField(blank=True)),
                ('intervention_estimate_time', models.DateField(blank=True)),
                ('intervention_leak_tool', models.CharField(blank=True, max_length=50)),
                ('intervention_type', models.CharField(choices=[('Hight', 'Hight'), ('Simple', 'Simple'), ('PipeSearch', 'Pipesearch')], default='Simple', max_length=50)),
                ('intervention_status', models.CharField(choices=[('NotStart', 'Notstart'), ('Pending', 'Pending'), ('Completed', 'Completed')], default='NotStart', max_length=50)),
                ('intervention_date', models.DateField(blank=True, default=django.utils.timezone.now)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=15)),
                ('is_published', models.CharField(choices=[('Published', 'Is Published'), ('Not Published', 'Is Not Published')], default='Not Published', max_length=50)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contracts.contract')),
            ],
        ),
    ]
