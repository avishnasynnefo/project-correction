from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

form_data = {
        'dep_list': department.objects.all()
    }

@login_required
def Table(request):
    if request.user.is_authenticated:
        d = {
        "datas": Tables.objects.all() 
        }
        return render(request,'index.html',d)
    else:
        return redirect(userlogin)



def delete(request,s_id):
    delete_field= Tables.objects.get(id=s_id)
    delete_field.delete()
    return redirect(Table)


def Registration(request):
   
    if request.method=="POST":
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        dob_= request.POST.get('dob')
        mail= request.POST.get('mail')
        phn_= request.POST.get('phn')
        dept_name= request.POST.get('dept')

        obj= Tables(Fname= fname,Lname=lname,Dob=dob_,email=mail,phn=phn_,dept=dept_name)
        obj.save()
        return redirect(Table)
    return render(request,'Register.html',form_data)

def Change(request,s_id):
    edit_field = Tables.objects.get(id=s_id)
    if request.method== 'POST':
        fname= request.POST.get('fname')
        lname= request.POST.get('lname')
        dob_= request.POST.get('dob')
        mail= request.POST.get('mail')
        phn_= request.POST.get('phn')
        dept_name= request.POST.get('dept')

        Tables.objects.filter(id=s_id).update(Fname= fname,Lname=lname,Dob=dob_,email=mail,phn=phn_,dept=dept_name)
        return redirect(Table)

    return render(request,'update.html')


def Create(request):
    if request.user.is_authenticated:
        return render(request,'create.html')
    else:
        if request.method=="POST":
           first_name =request.POST.get('fname')
           last_name =request.POST.get('lname')
           username = request.POST.get('username')
           email =request.POST.get('email')
           password =request.POST.get('password')

           if User.objects.filter(username=username, email=email).exists():
               messages.info(request,'username already taken')
               print(" account already have")
           else:
               new_user= User.objects.create_user(username,email,password )   
               new_user.first_name = first_name
               new_user.last_name = last_name
               new_user.save()
               return redirect(userlogin)

        return render(request,'create.html')
    
def userlogin(request):
    if request.method =="POST":
        username= request.POST.get('username')
        password=  request.POST.get('password')

        
        user=authenticate(request,username=username,password=password)
        
        if user is not None:
            login(request,user)
            #return render(request, 'index.html')
            return redirect(Table)
            # return redirect(')
        
        else:
            messages.info(request,'user not exits')
            print('user not exist')
            #return render(request, 'index.html')
            return redirect(userlogin)
    
    return render(request,'login.html')
    
@login_required
def userlogout(request):
    logout(request)
    return redirect(userlogin)
