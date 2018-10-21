from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *



def home(request):
    return render(request,'html/home.html')

def resume(request):
    image_object = open("portfolio/static/resume.pdf","rb").read()
    return HttpResponse(image_object, content_type="application/pdf")


def aboutme(request):
    return render(request,'html/about_me.html')

def project(request):
    return render(request,'html/project.html')

