from django.shortcuts import render

# Create your views here.
def StartTest(response):
    context = {}
    return render(response, "startest.html", context)

def Test(response, item):
    context = {
        "item_num" : item,
        "nextitem_num": item+1,
    }
    return render(response, "testitem.html", context)