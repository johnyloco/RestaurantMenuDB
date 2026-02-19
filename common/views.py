from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    context = {"message": "Welcome to the Restaurant!"}
    return render(request, 'common/home.html', context)