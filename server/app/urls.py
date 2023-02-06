from django.contrib import admin
from django.urls import path, include
from app import views
urlpatterns = [
    path('', views.index, name= 'home'),
    path('edit/<int:todo_id>/', views.edit, name= 'edit'),
    path('delete/<int:todo_id>/', views.delete, name= 'delete'),
]