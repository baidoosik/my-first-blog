from django.shortcuts import render, render_to_response, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Comment, TimeStampModel, Category
from .forms import PostForm,CommentForm
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
from django.contrib.auth.decorators import login_required

# 첫 페이지
def first_page(request):
    return render(request,'registration/first.html')

#thankq list 페이지
def thankq_list_page(request):
    return render(request,'blog/thank_list.html')

# 제품별 list 페이지
def starbucks_list_page(request):
    posts = Post.objects.filter(category=Category.objects.get(name='starbucks')).order_by('created_date')
    return render(request, 'blog/starbucks_list.html',{'posts':posts})

def coffeebean_list_page(request):
    posts = Post.objects.filter(category=Category.objects.get(name='coffeebean')).order_by('created_date')
    return render(request, 'blog/coffeebean_list.html',{'posts':posts})

def cow_list_page(request):
    return render(request,'cow/cow_list.html')
#소개팅 게시 페이지
def man_new(request):
    if request.method == "POST":
        form = ManForm(request.POST)

        if form.is_valid():
            man = form.save(commit=False)
            man.save()
            return redirect('cow_finish')
    else:
        form = ManForm()
    return render(request, 'cow/man.html', {'form': form})

def woman_new(request):
    if request.method == "POST":
        form = WomanForm(request.POST)

        if form.is_valid():
            woman = form.save(commit=False)
            woman.save()
            return redirect('cow/finish', pk=post.pk)
    else:
        form = ManForm()
    return render(request, 'cow/woman.html', {'form': form})
def cow_finish(request):
    return render(request,'cow/finish.html')

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
@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


def post_list(request):
	posts =Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html',{'posts':posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.image_file.delete()
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)
