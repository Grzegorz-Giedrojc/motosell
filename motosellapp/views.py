from django.shortcuts import render
from django.utils import timezone
from .models import Oferta

def post_list(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    return render(request, 'motosellapp/post_list.html', {'posts': posts})
