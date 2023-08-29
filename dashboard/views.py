from django.shortcuts import render

# Create your views here.
def Dashboard(response):
    context = {}
    return render(response, "dashboard.html", context)