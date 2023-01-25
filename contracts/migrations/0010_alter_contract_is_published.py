# Generated by Django 3.2.16 on 2023-01-25 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0009_alter_contract_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='is_published',
            field=models.CharField(choices=[('Published', 'Is Published'), ('Not Published', 'Is Not Published')], default='Not Published', max_length=50),
        ),
    ]