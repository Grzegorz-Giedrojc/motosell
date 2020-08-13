from django.shortcuts import render
from django.utils import timezone
from .models import Oferta
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from motosell1.settings import MEDIA_ROOT, MEDIA_URL
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def post_list(request):
    posts = Oferta.objects.filter(data_dodania__lte=timezone.now()).order_by('data_dodania')
    posts = Oferta.objects.filter(status='aktualny')

    return render(request, 'motosellapp/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Oferta, pk=pk)
    return render(request, 'motosellapp/post_detail.html', {'post': post})

@login_required(login_url="/accounts/login/")
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
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
    post = Oferta.objects.get(Oferta, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.uzytkownik = request.user
            post.data_publikacji = timezone.now()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'motosellapp/post_detail.html', {'form': form})

@login_required(login_url="/accounts/login/")
def my_posts(request):
    logged_in_user = request.user
    logged_in_user_posts = Oferta.objects.filter(uzytkownik=request.user)

    return render(request, 'motosellapp/my_posts.html', {'posts': logged_in_user_posts})

@login_required(login_url="/accounts/login/")
def update_post(request, pk):
    template = 'motosellapp/update_post.html'
    post = get_object_or_404(Oferta, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        try:
            if form.is_valid():
                form.save()
                messages.success(request, 'Zedytowano')
        except Exception as e:
            messages.warning(request, 'Edycja nieudana'.format(e))
    else:
        form = PostForm(instance=post)

    contex= {
    'form': form,
    'post': post,
    }

    return render(request, template, contex)
