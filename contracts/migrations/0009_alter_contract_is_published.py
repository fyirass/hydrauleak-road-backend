# Generated by Django 3.2.16 on 2023-01-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0008_alter_contract_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='is_published',
            field=models.CharField(choices=[('is_published', 'Is Published'), ('is_not_published', 'Is Not Published')], default='is_not_published', max_length=50),
        ),
    ]