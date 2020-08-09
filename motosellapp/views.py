from django.shortcuts import render
from django.utils import timezone
from .models import Oferta
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    return render(request, 'motosellapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Oferta, pk=pk)
    return render(request, 'motosellapp/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'motosellapp/post_edit.html', {'form': form})

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
