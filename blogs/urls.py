from django.urls import path
from blogs import views

urlpatterns = [
    path('home/', views.homePage,name="blogs-home"),
    path('about/', views.aboutPage,name="blogs-about"),
]
