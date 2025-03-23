from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [

    path('',views.display_index),

    path('user_register/',views.display_user_registration),
    path('user_registration/', views.user_registration),
]
