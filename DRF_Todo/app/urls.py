from django.urls import path
from .views import *
from rest_framework import routers


urlpatterns = [
    path('',TodoViewSet.as_view({'get':'list','post':'create'}), name='todo-list-create'),
]
