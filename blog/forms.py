import re
from django.contrib.auth.models import User
from django import forms
from .models import Post, Comment, Category, Datestyle1,Datestyle2,Man,Woman,Manstyle,Womanstyle
from django.contrib.auth.forms import UserCreationForm


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','category','가격','image_file','text',)

# 소개팅 form
class ManForm(forms.ModelForm):

    class Meta:
        model = Man
        exclude = ('created_at', )

class WomanForm(forms.ModelForm):

    class Meta:
        model = Woman
        exclude = ('created_at', )

class RegistrationForm(UserCreationForm):

	Emailaddress =forms.EmailField(label='이메일',)
	Phone_number = forms.CharField(label='휴대폰 번호',help_text=" -제외한 휴대폰 번호를 입력해주세요.")



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

