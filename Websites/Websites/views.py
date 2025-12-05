from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def render_page(request):    
    if request.method == "POST":      

        username = request.POST.get("username")
        password = request.POST.get("password")

        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)    # Logs the user in  
                      
            return HttpResponse(f"Welcome {username}! You are logged in.")
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def register_page(request):
    if request.method == "POST":
        # 1) Get form values
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 2) Check passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        # 3) Optional: small password rule
        if len(password1) < 6:
            messages.error(request, "Password should be at least 6 characters")
            return render(request, "register.html")

        # 4) Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")

        # 5) Create user (Django handles password hashing here)
        User.objects.create_user(username=username, password=password1)

        # 6) After register, go to login page
        return redirect("login")

    # If GET request → just show empty form
    return render(request, "register.html")




