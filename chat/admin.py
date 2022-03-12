from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['userName', 'timestamp', 'message']
    def userName(self, obj):
        return obj.user.user.username