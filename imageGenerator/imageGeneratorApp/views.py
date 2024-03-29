from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from .models import Person
from django.contrib.auth.models import User,AnonymousUser
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.method=="POST":
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        password=request.POST.get("password")
        role=request.POST.get("role")
        print(email, phone, password, role)
        obj=Person()  #This code creates an instance of the Person model (assuming it exists) and assigns values to its attributes.
        obj.email=email
        obj.role=role
        obj.password=password
        obj.phone=phone
        if Person.objects.filter(email=email).exists():
            messages.info(request, 'Account already exists')
            return redirect('signup')
        else:
            has_upper = any(char.isupper() for char in password)
            has_lower = any(char.islower() for char in password)
            has_digit = any(char.isdigit() for char in password)
            has_special_char = any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/? " for char in password)
            if(len(password)<8):
                messages.info(request,"Password must be atleast 8 characters")
                return redirect("signup")
            if(has_upper==False):
                messages.info(request,"Password must contain atleast one uppercase letter")
                return redirect("signup")
            if(has_lower==False):
                messages.info(request,"Password must contain atleast one lowercase letter")
                return redirect("signup")
            if(has_digit==False):
                messages.info(request,"Password must contain atleast one digit")
                return redirect("signup")
            if(has_special_char==False):
                messages.info(request,"Password must contain atleast one special character")
                return redirect("signup") 
            if(len(phone)!=10):
                messages.info(request,"Phone number should be of 10 digits")
                return redirect("signup")               
            obj.save()
            detail=Person.objects.all()   #partoapp_Person table entry
            #return redirect(request,"registration/login.html")
            user=User.objects.create_user(email=email, password=password,username=email)#auth_user table  entry
            #user_id = request.session.get('user_id')
            return redirect("signup")
            for i in detail:
                print(email)
    return render(request,"signup.html")


def loginView(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=authenticate(request,username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect("signup") 
        else:
            messages.info(request, "Incorrect credentials")
            return redirect("login")
    return render(request,"login.html")

def home(request):
    return render(request,"home.html")

def landing(request):
    return render(request,"landing.html")

def about(request):
    return render(request,"about.html")

def profile(request):
    return render(request,"profile.html")
