from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.http import HttpResponse
from .forms import ContactForm,LoginForm,CourseForm

from .models import Student,Course
# Create your views here.
def home_page(request):
    context={
        'name':'Shubham',
        'content':'Welcome to Home page'
    }
    return render(request,'home.html',context)

def about_page(request):
    context = {
        'name': 'Shubham',
        'content': 'Welcome to about page'
    }
    return render(request,'about.html',context)

def services_page(request):
    context = {
        'name': 'Shubham',
        'content': 'Welcome to service page'
    }
    return render(request,'services.html',context)

def register_page(request):
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():
            fname=request.POST.get('fname', '')
            lname=request.POST.get('lname', '')
            username=request.POST.get('username', '')
            password=request.POST.get('password', '')
            email=request.POST.get('email', '')
            mobile=request.POST.get('mobile', '')
            person=Student(fname=fname,lname=lname,username=username,password=password,email=email,mobile=mobile)
            person.save()
            return redirect('/#/')
    else:
        form=ContactForm()
        return render(request,'myregister.html',{'rform':form})

def login_page(request):
     if request.method=="POST":
         login_form=LoginForm(request.POST)
         if login_form.is_valid():
             username2=request.POST.get('username','')
             password2=request.POST.get('password','')
             dbuser=Student.objects.filter(username=username2,password=password2)
             if dbuser:
                 return redirect('/home/')
             else:
                 return redirect('/#/')
     else:
         login_form=LoginForm()
         return render(request,'login.html',{'login_form':login_form})

def course_page(request):
    if request.method=="POST":
        form=CourseForm(request.POST)
        if form.is_valid():
            fname=request.POST.get('fname', '')
            lname=request.POST.get('lname', '')
            cname=request.POST.get('cname', '')
            email=request.POST.get('email', '')
            mobile=request.POST.get('mobile', '')
            cperson=Course(fname=fname,lname=lname,cname=cname,email=email,mobile=mobile)
            cperson.save()
            return redirect('/thank/')
    else:
        form=CourseForm()
        return render(request,'contacts.html',{'cform':form})

def thank_page(request):
    context = {
        'name': 'Shubham',
        'content': 'you are successfully registered,Thanks'
    }
    return render(request,'thank.html',context)

