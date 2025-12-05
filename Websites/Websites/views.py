from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

def render_page(request):    
    if request.method == 'POST':
        user_name=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=user_name,password=password)
        if user != None:
            login(request,user)
            
            return render(request,'register.html')
        else:
            return "invalid login details"
    return render(request, 'Login.html')        


def register_page(request):
    if request.method == "POST":
        # 1) Get form values
        user_name=request.POST.get("username")
        pass_word1=request.POST.get("password1")
        pass_word2=request.POST.get("password2")
        # 2) Check passwords match
        if pass_word1!=pass_word2:
            messages.error(request,"the password did not match")
            return render(request,"register.html")          
        # 3) Optional: small password rule
        # if len(pass_word1) < 6:
        #     messages.error(request,"the password should contain atlease 6 digits")
        #     return render(request,"register.html")
        # 4) Check if username already exists
        if User.objects.filter(username=user_name).exists():
            messages.error(request, "User already exist")
            return render(request,'register.html')
        else:
            User.objects.create_user(username=user_name,password=pass_word1)
            return render(request,"Login.html")       
    # If GET request → just show empty form
    return render(request, "register.html")

