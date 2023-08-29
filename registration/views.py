from django.shortcuts import render

# Create your views here.
def Login(response):
    context = {}
    return render(response, "login.html", context)

def Register(response):
    context = {}
    return render(response, "register.html", context)