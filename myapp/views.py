from django.shortcuts import render

# Create your views here.

def Typing_speed(request):
    return render(request,"myapp/typing.html")