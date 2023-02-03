from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('', views.index, name= 'home'),
    path('edit', views.edit, name= 'edit')
]