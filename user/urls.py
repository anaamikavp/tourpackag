from django.contrib import admin
from django.urls import path,include
from user import views

urlpatterns = [

    path('',views.display_index),

    path('user_register/',views.display_user_registration),
    path('user_registration/', views.user_registration),
    path('login/',views.display_login),
    path('sign_in/',views.login),
    path('vendor_home/',views.view_vendor_index),
    path('show_packages/',views.display_packages),

]
