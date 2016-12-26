from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import image_cropping.fields

#소개팅 모델
class Person(models.Model):
    #기본정보
    name = models.CharField(max_length=20,null=False)
    age = models.CharField(max_length=20,null=False)
    email = models.EmailField(max_length=100,null=False)
    number =  models.CharField(max_length=20,null=False)
    #성향
    tendency = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Manstyle(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

class Womanstyle(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Datestyle1(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Datestyle2(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Man(Person):
    #성향
    mystyle =  models.ForeignKey(Manstyle, default='')
    major = models.CharField(max_length=30,null=False)

    womanstyle = models.ForeignKey(Womanstyle, null=True)
    datestyle1 = models.ForeignKey(Datestyle1, null=False)
    datestyle2 = models.ForeignKey(Datestyle2, null=False)
    anything = models.TextField(null=True)

    def __str__(self):
        return self.name

class Woman(Person):
    #성향
    mystyle =  models.ForeignKey(Womanstyle, default='')
    major = models.CharField(max_length=30,null=False)

    manstyle = models.ForeignKey(Manstyle, null=True)
    datestyle1 = models.ForeignKey(Datestyle1, null=False)
    datestyle2 = models.ForeignKey(Datestyle2, null=False)
    anything = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

# 쿠폰 모델

class TimeStampModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class Category(TimeStampModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(TimeStampModel):
    category = models.ForeignKey(Category, null=True)
    author = models.ForeignKey('auth.User')
    image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y/%m/%d')
    title = models.CharField(max_length=200,null=False)
    text = models.TextField()

    published_date = models.DateTimeField(blank=True, null=True)

    # size is "width x height
    #cropimage = ImageRatioField('image_file', '430x360')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(TimeStampModel):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
    def approved_comments(self):
        return self.comments.filter(approved_comment=True)
    def __str__(self):
        return self.text
