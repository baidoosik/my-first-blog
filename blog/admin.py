from django.contrib import admin
from .models import Post, Comment, Category, Datestyle1,Datestyle2,Man,Woman,Manstyle,Womanstyle

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']
    list_display_links =['title']


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Datestyle1)
admin.site.register(Datestyle2)
admin.site.register(Manstyle)
admin.site.register(Womanstyle)
admin.site.register(Man)
admin.site.register(Woman)




# Register your models here.
