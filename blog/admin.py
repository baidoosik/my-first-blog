from django.contrib import admin
from .models import Post, Comment, Category, Datestyle1,Datestyle2,Man,Woman,Manstyle,Womanstyle

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'category', 'title' ]
    list_display_links =['title']
    list_filter = ['published_date', 'category']
    search_fields =  ['title']

admin.site.register(Comment)
admin.site.register(Category)
#소개팅
admin.site.register(Datestyle1)
admin.site.register(Datestyle2)
admin.site.register(Manstyle)
admin.site.register(Womanstyle)
admin.site.register(Man)
admin.site.register(Woman)




# Register your models here.
