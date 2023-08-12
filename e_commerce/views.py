from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def handleSignUp(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # check for errorneous input
        if len(username) > 10:
            messages.error(request, "user name must be less than 10 character")
            return redirect('/shop')
        if not username.isalnum():
            messages.error(request, "user name must be alphanumeric")
            return redirect('/shop')
        if pass1 != pass2:
            messages.error(request, "password do not match")
            return redirect('/shop')


        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "Your FlashKart account has been successfully created")
        return redirect('/shop')

    else:
        return HttpResponse("404 - Not found")

def handleLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/shop")
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("/shop")

    return HttpResponse("404- Not found")


def handleLogout(request):
        logout(request)
        messages.success(request, "Successfully Logged Out")
        return redirect("/shop")
