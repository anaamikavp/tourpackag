from django.contrib import admin
from django.urls import path,include
from vendor import views

urlpatterns = [
    path('register/',views.register),
    path('vendor_registration/', views.vendor_registration)
]
