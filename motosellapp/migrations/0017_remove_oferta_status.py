# Generated by Django 3.1 on 2020-08-12 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('motosellapp', '0016_oferta_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oferta',
            name='status',
        ),
    ]