# Generated by Django 3.2.16 on 2023-02-01 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20230201_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='zone_color',
            field=models.CharField(choices=[('#97c900', 'Green'), ('orange', 'Orange'), ('#ff1919', 'Red')], default='orange', max_length=20),
        ),
    ]