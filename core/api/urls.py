from django.contrib import admin
from django.urls import path

from quickstart.views import index,person

urlpatterns = [
    path('index/', index),
    path('person/',person)
]
