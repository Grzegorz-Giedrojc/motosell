from django.shortcuts import render
from django.utils import timezone
from .models import Oferta
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from motosell1.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    return render(request, 'motosellapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Oferta, pk=pk)
    return render(request, 'motosellapp/post_detail.html', {'post': post})

@login_required(login_url="/accounts/login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.uzytkownik = request.user
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'motosellapp/post_edit.html', {'form': form})

@login_required(login_url="/accounts/login/")
def post_edit(request, pk):
    post = get_object_or_404(Oferta, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.uzytkownik = request.user
            post.data_publikacji = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'motosellapp/post_edit.html', {'form': form})

def my_posts(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    current_user = request.POST.get('uzytkownik')
    user_posts = Oferta.objects.filter(uzytkownik=current_user)

    return render(request, 'motosellapp/my_posts.html', {'posts': posts})
