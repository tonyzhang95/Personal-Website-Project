from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'password_generator'

urlpatterns = [
    path('', views.generator, name='generator'),
    path('password/', views.password, name='password'),
]
