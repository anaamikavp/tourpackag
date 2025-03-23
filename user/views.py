import hashlib

from django.shortcuts import render

from user.models import register_table
from datetime import datetime


def display_index(request):
    return render(request,'index.html')

def display_user_registration(request):
    return render(request,'register.html')


def user_registration(request):
    if request.method=="POST":

        #get data from form
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email_address")
        password=request.POST.get("password")
        confirm_password=request.POST.get("repeat_password")

    #variables to pass errors
        email_error=""
        password_error=""
        confirm_password_error=""

        flag=0 # variable to check if the form is valid or  not

        data=register_table.objects.all()    #get data from register_table from data base

        #validation
        #checking email already exists or  not
        for i in data:
            if email==i.email:
                email_error="Email already exists"
                flag=1

        if len(password)<8:
            password_error="Password should contain atleast 8 characters"
            flag=1

        if password!=confirm_password:
            confirm_password_error="Password and Confirm password should be same"
            flag=1

        if flag==1:
            return render(request,'register.html',{"e_error":email_error, "p_error":password_error, "cp_error":confirm_password_error})
        else:
        #object for register_table
            user_data=register_table()
            user_data.firstname=first_name
            user_data.lastname=last_name
            user_data.email=email
            user_data.password=hashlib.sha1(password.encode('utf-8')).hexdigest()  #encrypt password
            user_data.user_type='user'
            user_data.created_at=datetime.now()
            user_data.updated_at=datetime.now()
            user_data.save()
            return render(request,'index.html')











# Create your views here.
