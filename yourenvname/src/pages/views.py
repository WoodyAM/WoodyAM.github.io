from django.shortcuts import render

# Create your views here.

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def pitch_view(request, *args, **kwargs):
     return render(request, "pitch.html", {})

def catch_view(request, *args, **kwargs):
    return render(request, "catch.html", {})

def profile_view(request, *args, **kwargs):
    return render(request, "profile.html", {})

