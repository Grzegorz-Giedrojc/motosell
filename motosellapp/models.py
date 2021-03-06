from django.db import models
from django.utils import timezone



# Create your models here.

class Oferta(models.Model):
    id=models.AutoField(primary_key=True)
    tytul=models.CharField(max_length=100)
    opis=models.TextField()

    MOTOCYKL='motocykl'
    OSOBOWY='osobowy'
    CIEZAROWY='ciezarowy'
    KATEGORIA=[
        (MOTOCYKL, ('motocykl')),
        (OSOBOWY, ('osobowy')),
        (CIEZAROWY, ('ciezarowy'))
    ]
    kategoria=models.CharField(
        max_length=32,
        choices=KATEGORIA,
        default=OSOBOWY,
    )
    marka=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    rok_produkcji=models.IntegerField()
    przebieg=models.IntegerField()
    pojemnosc_skokowa=models.IntegerField()

    BENZYNA='benzyna'
    DIESEL='diesel'
    LPG='LPG'
    RODZAJ_PALIWA=[
        (BENZYNA, ('benzyna')),
        (DIESEL, ('diesel')),
        (LPG, ('LPG'))
    ]
    rodzaj_paliwa=models.CharField(
        max_length=32,
        choices=RODZAJ_PALIWA,
        default=BENZYNA,
    )
    uzytkownik=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    zdjecie=models.ImageField(default='default.png')
    koszt=models.IntegerField()
    kontakt=models.IntegerField(default=123456789)
    data_dodania=models.DateTimeField(default=timezone.now)
    data_publikacji=models.DateTimeField(blank=True, null=True)
    AKTUALNY='aktualny'
    NIEAKTUALNY='nieaktualny'
    STATUS=[
        (AKTUALNY, ('aktualny')),
        (NIEAKTUALNY, ('nieaktualny')),
    ]
    status=models.CharField(
        max_length=32,
        choices=STATUS,
        default=AKTUALNY,
    )


    def publish(self):
        self.data_dodania=timezone.now()
        self.save()

    def __str__(self):
        return self.tytul
