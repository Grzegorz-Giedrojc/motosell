# Generated by Django 3.1 on 2020-08-13 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motosellapp', '0021_auto_20200813_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='kontakt',
            field=models.IntegerField(default=123456789),
        ),
    ]
