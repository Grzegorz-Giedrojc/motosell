from django import forms

from .models import Oferta

class PostForm(forms.ModelForm):

    class Meta:
        model = Oferta
        fields = ('tytul', 'opis', 'kategoria', 'marka', 'model', 'rok_produkcji', 'przebieg', 'pojemnosc_skokowa', 'rodzaj_paliwa','koszt', 'kontakt', 'uzytkownik', 'zdjecie', 'data_dodania', 'data_publikacji', 'status')
