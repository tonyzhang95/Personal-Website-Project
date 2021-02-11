from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.todo, name='todo'),
]
