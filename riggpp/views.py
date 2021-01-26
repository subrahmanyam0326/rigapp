from django.shortcuts import render
from django.http import HttpResponse
def view(request):
    x="hello this sis subbu"
    return  HttpResponse(x)
