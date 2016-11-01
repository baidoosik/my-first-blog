from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(forms.Form):
	usename = forms.CharField(label='사용자이름',max_length=30)
	email =forms.EmailField(label='e-mail')
	password1 = forms.CharField(label='비밀번호',widget=forms.PasswordInput())
	password2 = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput())	