# Generated by Django 3.1 on 2020-08-09 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motosellapp', '0002_oferta_rodzaj_paliwa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='pojemnosc_skokowa',
            field=models.FloatField(),
        ),
    ]
