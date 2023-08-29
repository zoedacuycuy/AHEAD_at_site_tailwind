from django.shortcuts import render

# Create your views here.
def Feedback(response):
    context = {}
    return render(response, "feedback.html", context)