from django.contrib import admin
from django.urls import path
from .views import registeration, login

urlpatterns = [
    path('register/', registeration),
    path('login/', login)
]
