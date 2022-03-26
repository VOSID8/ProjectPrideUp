from csv import list_dialects
from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'authorName', 'date', 'views']
    def authorName(self, obj):
        return obj.author.user.username


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'date', 'postTitle', 'authorName']
    def postTitle(self, obj):
        return obj.post.title
    
    def authorName(self, obj):
        return obj.author.username
