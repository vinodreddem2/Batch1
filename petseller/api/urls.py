
from django.contrib import admin
from django.urls import path,include
from home.views import AnimalView

urlpatterns = [
    path('animal/',AnimalView.as_view())
]
