from django.contrib import admin
from django.urls import path
from myapp import views  # Import the view from your app

urlpatterns = [
    path('', views.index, name='index'),  # Empty path
]
