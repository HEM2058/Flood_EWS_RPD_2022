from django.shortcuts import render,redirect
from myapp.models import *
from random import randint
# Create your views here.


def Index(request):
    # if 'id' in request.session:
    #       id = request.session.get('id')
    #       if id:
    #        user = User.objects.get(id=id)
    #        return render(request,"index.html",{'user':user})
    #       else:
           return render(request,"index.html")



def RegisterForm(request):
    return render(request,"guide/index.html")

def Register(request):
    if (request.method == "POST"):
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        password = request.POST["password"]
        cpassword = request.POST.get("cpassword")
        lat =request.POST["lat"]
        lng = request.POST["lng"]
        

        user = User.objects.filter(email=email)
        if user:
            msg = "User with this email address is already exist !"
            return render(request,"guide/index.html",{'msg':msg})

        else:

         if(password == cpassword):
            otp = randint(100000,999999)
            user = User.objects.create(fname=fname,lname=lname,email=email,phone=phone,password=password,lat=lat,lng=lng,otp=otp,)
            return render(request,"guide/otpmail.html",{'email':email})

def OtpPage(request):
     return render(request,"guide/otpmail.html")

def OtpConfirm(request):
     email = request.POST.get('email')
     otp = int(request.POST.get('otp'))
     user = User.objects.get(email=email)
     if user:
        if user.otp==otp:
           message = "Otp verify successfully"
           return render(request,'guide/loginpage.html',{'msg':message}) 
        else:
             message = "Otp is incorrect"
             return render(request,'guide/otpmail.html',{'msg':message}) 
        
     else:
      return render(request,'guide/index.html')
    
def LoginPage(request):
    return render(request,"guide/loginpage.html")

def Loginuser(request):
    if request.method == "POST":
      email = request.POST.get('email')
      password = request.POST.get('password')
                                               
      user = User.objects.get(email=email)
      if user:
        if user.password == password:
          request.session['id'] = user.id
          request.session['email'] =  user.email
          request.session['fname'] = user.fname
          request.session['lname'] =  user.lname
          
          return redirect('index')
        
        else:
         if user.password != password:
            message = "Password doesnot match"
            return render(request,'guide/loginpage.html',{'msg':message})
        
      else:
        message = "User doesnot exist"
        return render(request,'guide/loginpage.html',{'msg':message})

