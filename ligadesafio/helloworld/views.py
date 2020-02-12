from django.shortcuts import render
from django.http import HttpResponse


def helloworld(request):
    return render(request, 'helloworld/helloworld.html')
# Create your views here.
