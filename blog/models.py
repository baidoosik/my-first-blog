from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import image_cropping.fields
"""
from categories.registration import register_fk

categories.register_fk(Post, 'coffee')
categories.register_fk(Post, 'starbucks', {'related_name':'kind1'})
categories.register_fk(Post, 'coffeebean', {'related_name':'kind2'})
"""
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
