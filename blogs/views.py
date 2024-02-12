from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
posts=[
     {
         'author':'Shahzadi Bakhtawar',
         'title':'Blog post 1',
         'content':'First post content',
         'date_posted':"January 31, 2022"
     },
      {
         'author':'Shahzada Cloudie',
         'title':'Blog post 2',
         'content':'Second post content',
         'date_posted':"November 25, 2018"
     }
 ]

def homePage(request):
    context={
        'posts':posts,
        "mainTitle":"Science"
    }
    return render(request,'blogs/home.html',context)

def aboutPage(request):
    return render(request,'blogs/about.html',{'mainTitle':"About"})