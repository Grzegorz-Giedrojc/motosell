# Generated by Django 3.1 on 2020-08-06 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tytul', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('kategoria', models.CharField(choices=[('motocykl', 'motocykl'), ('osobowy', 'osobowy'), ('ciezarowy', 'ciezarowy')], default='osobowy', max_length=32)),
                ('marka', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('rok_produkcji', models.IntegerField()),
                ('przebieg', models.IntegerField()),
                ('pojemnosc_skokowa', models.IntegerField()),
                ('zdjecie', models.ImageField(upload_to='')),
                ('data_dodania', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_publikacji', models.DateTimeField(blank=True, null=True)),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
