from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('BBS page')

def write(request):
    return HttpResponse('Write')

def register(request):
    return HttpResponse('Register')

def read(request, article_id):
    return HttpResponse('Read' + article_id)