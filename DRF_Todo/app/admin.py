from django.contrib import admin
from .models import *

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')
    list_filter = ('completed',)
    search_fields = ('title',)

admin.site.register(Todo,TodoAdmin)