from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate ,login as user_login ,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render
from Packages_Plan.models import Laundary_Packages
from Shoe_Packages_Plan.models import Shoe_Packages_Plan
from Packages_Section.models import Packages_Section














def home(request):
    laundary_packages = Laundary_Packages.objects.all()
    shoe_packages = Shoe_Packages_Plan.objects.all()
    packages_section = Packages_Section.objects.all()

    Data ={
        "laundary_packages_data" : laundary_packages,
        "shoe_packages_data" : shoe_packages,
        "packages_section_data" : packages_section,
    }
    return render(request, 'index.html', Data)



def login(request):
    return render(request, 'login.html')



def sign_up(request):
    return render(request, 'sign-up.html')


def orders(request):
    return render(request, 'orders.html')



def dashboard(request):
    return render(request, 'dashboard.html')








def Create_account(request): 
    user_name = request.POST['username']
    user_email = request.POST['email']
    user_password = request.POST['password']

    if user_name == '' or user_email == '' or user_password == '':
        messages.error(request, "Please fill all fields.")
        return redirect('sign-up')

    if len(user_password) != 8:
        print("wrong")
        # messages.error(request, "Password must be exactly 8 characters long.")
        return redirect('sign-up')


        
    user = User.objects.create_user(username=user_name, email=user_email,  password=user_password)
    return render(request, 'login.html')






def loginUser(request):
    
    user_name = request.POST['username']
    user_password = request.POST['password']

    if user_name == '' or user_password == ''  :
        messages.error(request, "Please provide the email and password")
        return redirect('login')
    user = authenticate(request, username=user_name, password=user_password)
  
    if user is not None:
         user_login(request, user)
         request.session['username'] = user.username
         request.session['password'] = user.password
         return redirect('/')
    else:
        print("User doesn't exist")
        messages.error(request, "User does not exit")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')