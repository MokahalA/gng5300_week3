from django.shortcuts import render

def signup_view(request):
    return render(request, 'signup/signup.html')

def login_view(request):
    return render(request, 'signup/login.html')