# Generated by Django 3.2.16 on 2023-02-28 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20230227_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='intervention',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='maps.map'),
        ),
    ]
