from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.db.models import Q, Model
from django.db import connection, models 
from django.db import IntegrityError
from .models import user_details,user_images
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']
        if username == "" or password == "" or password2 =="" or email == "":
            messages.info(request, "please fill up all the fields")
            print("please fill up all fields")
            return redirect('signup')
        elif User.objects.filter(username=username).exists():
            messages.info(request, "user name taken")
            print("username taken")
            return redirect('signup')
        elif password != password2:
            messages.info(request, "password error")
            print("password error ")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email taken")
            print("email.taken")
            return redirect('signup')
        else:
            user = User.objects.create_user(
            username=username, password =password)
            user.save()
            auth.login(request, user)
            return redirect(home)
    return render(request, 'signup.html')



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(home)
        else:
            messages.info(request, "username mismatch ")
            print("username mismatch")
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    
    


def home(request):
    det=user_images()
    det=user_images.objects.all()
    return render(request,'home.html',{'det':det})
def profile(request):
    apps=user_details.objects.all()
    return render(request,'profile.html',{'apps':apps})

def details(request):
    if request.method == 'POST':
        firstname= request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phonenumber=request.POST.get('phonenumber')
        if firstname == "" or lastname=="" or email == "" or phonenumber =="":
            messages.info(request, "please fill up all the fields")
            print("please fill up all fields")
            return redirect('details')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "emailid  already exists")
            print("email taken")
            return redirect('last')
        else :
            apps = user_details(
            firstname=firstname, lastname=lastname,email=email,phonenumber=phonenumber)
            apps.save()
            return redirect('/last')
    else:
        return render(request, 'details.html',)



def last(request):
    return render(request, 'last.html')
def logout(request):
    auth.logout(request)
    return redirect("signup")
