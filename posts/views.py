from django.contrib.auth import logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login
from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User

from .models import Post


@login_required
def index(request):
    postlist = Post.objects.all().order_by('-post_pub_date')[:]
    return render(request, 'posts/board.html', {'postlist': postlist})


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def logout(request):
    django_logout(request)
    return render(request, 'registration/logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse("index"))
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@csrf_protect
@login_required
def add_new_post(request):
    if request.POST:
        new_post_input = {
            "post_title": request.POST.get("title"),
            "post_desc": request.POST.get("message"),
            "post_author": request.POST.get("author"),
            "post_pub_date": request.POST.get("date")
        }
        new_post = Post.objects.create(**new_post_input)
        return HttpResponseRedirect("/")
    else:
        return render(request, "posts/board.html")
