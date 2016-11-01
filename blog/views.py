from django.shortcuts import render
from django.shortcuts import render_to_response
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from blog.forms import *
from django.template import RequestContext

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if  form.is_valid():
            user =User.objects.create_user(
                username= form.cleaned_data['username'],
                email= form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form =RegistrationForm()

    variables = RequestContext(request,{
        'form': form
    })

    return render_to_response('registration/register.html',variables)
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
    