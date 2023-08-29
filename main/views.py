from django.shortcuts import render

# Create your views here.
def LandingPage(response):
    context = {}
    return render(response, "landing_page.html", context)

def About(response):
    context = {}
    return render(response, "about.html", context)

def Login(response):
    pass