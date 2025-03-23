from django.contrib import admin
from django.urls import path,include
from vendor import views

urlpatterns = [
    path('register/',views.register),

]
