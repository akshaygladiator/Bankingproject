from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.



def Home(request):
    return render(request,"Home.html")

def Form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        # if user is not None:
        auth.login(request, user)
        messages.info(request, "application accepted")
        return redirect('Form')
    return render(request, "Form.html")
 #       name = request.POST['name']
 #        DOB = request.POST['DOB']
 #       Age = request.POST['Age']
 #       Gender = request.POST['Gender']
 #       Contact = request.POST['Phone']
 #       Mail = request.POST['email']
 #       address = request.POST['address']
 #       Bank = request.POST['branch']
 #       Account = request.POST['account']
 #       Address = request.POST['address']
 #       Materials = request.POST['Materials to provide']
 #      user =  User.objects.create_user(name=name,DOB=DOB,Age=Age,Gender=Gender,Contact=Phone,Mail=email,address=address,Bank=branch,Account=account,Address=address,Materials=Materials to provide )
 #      if user is not None:
 #        auth.Form(request, user)
 #       user.save();
 #       messages.info(request, "application accepted")
 #    return redirect('Home')
 #   return render(request, "Home.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, "Newpage.html")
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")


def register(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
           if User.objects.filter(username=username).exists():
               messages.info(request, "Username Taken")
               return redirect('register')

           else:
                user = User.objects.create_user(username=username, password=password)

                user.save();
                return redirect('login')

        else:
           messages.info(request, "password not matching")
           return redirect('register')
        return redirect('/')
    return  render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')

def Newpage(request):
    auth.Newpage(request)
    return redirect('/')