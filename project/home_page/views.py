from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "home_page/home_page.html")

