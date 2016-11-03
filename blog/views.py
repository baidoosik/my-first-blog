from django.shortcuts import render, render_to_response
from django.utils import timezone
from .models import Post, Bookmark
from django.shortcuts import render, get_object_or_404,redirect
from .forms import PostForm
from django.http import HttpResponseRedirect, Http404,  HttpResponse
from django.contrib.auth import logout
from blog.forms import *
from django.template import RequestContext
from django.template.loader import get_template
import re
from django.contrib.auth.models import User
from django.template import Context
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

def register_page(request):
    if request.method == "POST":
        userform = UserCreationForm(request.POST)
        if userform.is_valid():
            userform.save()
        
            return HttpResponseRedirect(
                reverse("login")
            )
    elif request.method == "GET":
        userform =UserCreationForm()

    return render(request,'registration/register.html',{"userform":userform})

def user_page(request, username):
    try:
      user = User.objects.get(username=username)
    except:
      raise Http404('사용자를 찾을 수 없습니다.')

    template = get_template('user_page.html')
    variables= Context({
        'username': username
        })

    output= template.render(variables)
    return HttpResponse(output)

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
          
def post_list(request):
	posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
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
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    