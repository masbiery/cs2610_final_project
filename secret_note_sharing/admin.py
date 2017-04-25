from django.contrib import admin

# Register your models here.

from .models import Message

class Admin(admin.ModelAdmin):
    list_display = ('message_text','id',)
    
admin.site.register(Message,Admin)