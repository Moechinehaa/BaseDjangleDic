from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def he(request):
    print("he")
    return render(request,'sample.html')

def home(request):
    return HttpResponse("home page")