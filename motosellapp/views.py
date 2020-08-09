from django.shortcuts import render
from django.utils import timezone
from .models import Oferta
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    return render(request, 'motosellapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Oferta, pk=pk)
    return render(request, 'motosellapp/post_detail.html', {'post': post})
