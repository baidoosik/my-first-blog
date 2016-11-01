import re
from django.contrib.auth.models import User
from django import forms
from .models import Post
from django.core.exceptions import ObjectDoesNotExist

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class RegistrationForm(forms.Form):
	usename = forms.CharField(label='사용자이름',max_length=30)
	email =forms.EmailField(label='이메일')
	password1 = forms.CharField(label='비밀번호',widget=forms.PasswordInput())
	password2 = forms.CharField(label='비밀번호 확인',widget=forms.PasswordInput())

	def clean_username(self):
		username = self.cleaned_data['usename']
		if not re.search(r'^\w+$',username):
		  raise forms.ValidationError(
		  	'사용자 이름은 알파벳, 숫자, 밑줄(_)만 가능합니다.')
		try:
		  User.obejects.get(username=username)
		except ObjectDoesNotExist:
		  return username
		raise forms.ValidationError('이미 사용중 중인 사용자 이름!') 	