# Generated by Django 3.1 on 2020-08-12 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motosellapp', '0019_auto_20200812_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oferta',
            name='koszt',
            field=models.TextField(),
        ),
    ]
