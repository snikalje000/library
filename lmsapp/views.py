from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')

def adminclick(request):
    return render(request,'adminclick.html')

def adminafterlogin(request):
    return render(request,'adminafterlogin.html')

def admin1(request):
    return render(request,'admindash.html')

def adminsignup(request):
    return render(request,'adminsignup.html')

def studentpanel(request):
    return render(request,'studentpanel.html')

def studentsignup(request):
    return render(request,'studentsignup.html')

def studentlogin(request):
    return render(request,'studentlogin.html')

def studentafterlogin(request):
    return render(request,'studentafterlogin.html')

def addbook(request):
    return render(request,'addbook.html')

def listbook(request):
    return render(request,'listbook.html')

def issuebook(request):
    return render(request,'issuebook.html')

def panalty(request):
    return render(request,'panalty.html')

def viewissuebook(request):
    return render(request,'viewissuebook.html')

def viewissuebookbystudent(request):
    return render(request,'viewissuebookbystudent.html')


