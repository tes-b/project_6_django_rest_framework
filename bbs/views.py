from django.shortcuts import render, HttpResponse
from django.template import loader

# Create your views here.

def index(request):
    # return HttpResponse('BBS page')
    # template = loader.get_template('bbs/index.html')
    # context = {}
    # return HttpResponse(template.render(context,request))
    return render(request, "index.html")

def write(request):
    return HttpResponse('Write')

def register(request):
    return HttpResponse('Register')

def read(request, article_id):
    return HttpResponse('Read' + article_id)

def base(request):
    return HttpResponse('../templates/base.html')