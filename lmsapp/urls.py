"""lms1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from lmsapp import views

urlpatterns = [
    path('',views.index),
    path('adminclick/',views.adminclick),
    path('adminsignup/',views.adminsignup),
    path('adminafterlogin/',views.adminafterlogin),
    path('admin1/',views.admin1),
    path('studentpanel/',views.studentpanel),
    path('studentsignup/',views.studentsignup),
    path('studentlogin/',views.studentlogin),
    path('studentafterlogin/',views.studentafterlogin),
    path('addbook/',views.addbook),
    path('listbook/',views.listbook),
    path('issuebook',views.issuebook),
    path('panalty/',views.panalty),
    path('viewissuebook/',views.viewissuebook),
    path('viewissebookbystudent/',views.viewissuebookbystudent)
]
