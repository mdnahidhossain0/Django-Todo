from django.contrib import admin

from .models import Todo
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('srno', 'title', 'describtion', 'user', 'date')

admin.site.register(Todo, AuthorAdmin)