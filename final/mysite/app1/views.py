from argparse import Action
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def IndexPage(request):
    return render(request,'index.html')

@login_required(login_url='login')
def HomePage(request):
    return render(request,'home.html')

def SignupPage(request):
    if request.method=='POST':
       username = request.POST.get('username')
       email =request.POST.get('email')
       first_name =request.POST.get('first_name')
       last_name=request.POST.get('last_name')
       password = request.POST.get('password')
       password2 = request.POST.get('password2')

       if( password!=password2):
           return HttpResponse("Your password and conform password are not same")
       else:
           user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
           user.save()

           return redirect('login')
        
       
       
    return render(request,'signup.html')

def LoginPage(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("User name or password is incorrect")
            
    return render(request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def ToSignPage(request):
    return render(request,'tosign.html')

@login_required(login_url='login')
def AboutUsPage(request):
    return render(request,'aboutus.html')

@login_required(login_url='login')
def ToTextPage(request):
    return render(request,'totext.html')