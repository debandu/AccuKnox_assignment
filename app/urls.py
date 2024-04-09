from django.contrib import admin
from django.urls import path
from .views import save

urlpatterns = [
    path('save/',save.as_view(),name="save"),
]
