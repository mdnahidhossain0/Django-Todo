from django.urls import path, include
from .views import *
urlpatterns = [
    path('',Signup),
    path('login/',Login),
    path('todo/',Todoview),
    path('todo/edit/<int:id>/', edit_todo, name='edit_todo'),
    path('todo/delete/<int:id>/', delete_todo, name='delete_todo'),
]
