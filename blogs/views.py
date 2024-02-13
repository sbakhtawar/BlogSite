from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def homePage(request):
    context={
        'posts':Post.objects.all(),
        "mainTitle":"Blogs"
    }
    return render(request,'blogs/home.html',context)

def aboutPage(request):
    return render(request,'blogs/about.html',{'mainTitle':"About"})