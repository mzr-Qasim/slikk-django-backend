from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate ,login as user_login ,logout
from django.contrib.auth.models import User
from User_Profiles.forms import User_Custom_Form
from django.contrib import messages
from django.http import JsonResponse
import random
import string
from django.shortcuts import render
from Site_Settings.models import Site_Settings
from Packages_Plan.models import Packages_Plan
from Packages_Section.models import Packages_Section
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
import stripe
from django.conf import settings
from Orders.models import Order, OrderPackages







def home(request):
    site_settings = Site_Settings.objects.all()
    packages_plan = Packages_Plan.objects.all()
    packages_section = Packages_Section.objects.all()

    Data ={
        "site_settings_data": site_settings,
        "packages_plan_data" : packages_plan,
        "packages_section_data" : packages_section,
    }
    return render(request, 'index.html', Data)




def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        pass
    
    site_settings = Site_Settings.objects.all()
    Data ={
        "site_settings_data": site_settings,
    }
    return render(request, 'login.html', Data)



def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        pass

    site_settings = Site_Settings.objects.all()
    Data ={
        "site_settings_data": site_settings,
    }

    return render(request, 'sign-up.html',Data)





def orders(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    
    packages_plan = Packages_Plan.objects.all()
    

    Data ={
        "packages_plan_data" : packages_plan,
    }

    return render(request, 'orders.html',Data)


def checkout(request):
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')
    
    site_settings = Site_Settings.objects.all()
    cart= Cart(request)
    package_items= list(cart.session.values())[5]
    subtotal= 0
    for package in package_items:
        subtotal = subtotal + float(package_items[package]['price']) * int(package_items[package]['quantity'])
    

    if request.method == "POST":
        form = User_Custom_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= User_Custom_Form()

    gst = (subtotal*20/100)
    Total = (gst+subtotal)
    Data ={
        "site_settings_data": site_settings,
        "subtotal_value" : subtotal,
        "gst_value": gst,
        "total_value": Total,
        "form": form,
    }
    return render(request, 'checkout.html',Data)



def dashboard(request):


    user = request.user  # Get the currently logged-in user

    # Generate the referral code
    referral_code = generate_referral_code(user)
    if request.user.is_authenticated:
        pass
    else:
        return redirect('login')

    site_settings = Site_Settings.objects.all()
    Data ={
        "site_settings_data": site_settings,
        "referral_code": referral_code,
    }
    # Pass the referral code to the template
    return render(request, 'dashboard.html',Data)








def Create_account(request): 
    f_name = request.POST['first-name']
    l_name = request.POST['last-name']
    user_name = request.POST['username']
    user_email = request.POST['email']
    user_password = request.POST['password']
    user_password_verfication = request.POST['password-verification']

    if f_name == '' or l_name == '' or  user_name == '' or user_email == '' or user_password == '' or user_password_verfication == '':
        messages.error(request, "Please fill all fields.")
        return redirect('sign-up')
    
    if user_password != user_password_verfication:
        messages.error(request, "Password didn't match")
        return redirect('sign-up')
    
    if len(user_password) < 8:
        messages.error(request, "Password must be at least 8 characters long.")
        return redirect('sign-up')


        
    user = User.objects.create_user(first_name=f_name, last_name=l_name, username=user_name, email=user_email,  password=user_password)
    return render(request, 'login.html')






def loginUser(request):
    
    user_name = request.POST['username']
    user_password = request.POST['password']

    if user_name == '' or user_password == ''  :
        messages.error(request, "Please provide the username and password")
        return redirect('login')
    

    user = authenticate(request, username=user_name, password=user_password)
    if user is not None:
         user_login(request, user)
         request.session['username'] = user.username
         request.session['password'] = user.password
         return redirect('/')
    else:
        messages.error(request, "User does not exist")
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('home')


def generate_referral_code(user):
    # Generate a random 6-character string from uppercase letters and digits
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    # Combine the first 3 characters of the username with the random string
    referral_code = f"{user.username[:3].upper()}{random_string}"
    return referral_code





def cart_add(request, id):
    cart = Cart(request)
    product = Packages_Plan.objects.get(id=id)
    cart.add(product=product)
    return redirect("orders")



def item_clear(request, id):
    cart = Cart(request)
    product = Packages_Plan.objects.get(id=id)
    cart.remove(product)
    return redirect("orders")



def item_increment(request, id):
    cart = Cart(request)
    product = Packages_Plan.objects.get(id=id)
    cart.add(product=product)
    return redirect("orders")



def item_decrement(request, id):
    cart = Cart(request)
    product = Packages_Plan.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("orders")



def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("orders")



def cart_detail(request):
    site_settings = Site_Settings.objects.all()
    cart= Cart(request)
    package_items= list(cart.session.values())[5]
    subtotal= 0
    for package in package_items:
        subtotal = subtotal + float(package_items[package]['price']) * int(package_items[package]['quantity'])

    gst = (subtotal*20/100)
    Total = (gst+subtotal)
    Data ={
        "site_settings_data": site_settings,
        "subtotal_value" : subtotal,
        "gst_value": gst,
        "total_value": Total,
    }
    return render(request, 'orders.html', Data)




def create_checkout_session(request):
    cart= Cart(request)
    package_items= list(cart.session.values())[5]
    subtotal= 0
    for package in package_items:
        subtotal = subtotal + float(package_items[package]['price']) * int(package_items[package]['quantity'])
    

    if request.method == "POST":
        form = User_Custom_Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form= User_Custom_Form()

    gst = (subtotal*20/100)
    Total = (gst+subtotal)
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
        line_items =[{
            'price_data' :{
              'currency' : 'usd',  
              'unit_amount': int(Total*1000),
              'product_data': {
                  'Package': 'laundary premium',
                },
            },
            'quantity' : 1
        }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url= 'http://127.0.0.1:8000/cancel',
        )
        if checkout_session:
            order = Order.objects.create(user=request.user, total_price=Total, payment_id=checkout_session.id, payment_status= 'paid')
            if order:
                for package in package_items:
                    OrderPackages.objects.create(order=order, package_name=package_items[package]['name'],quantity=package_items[package],price=package_items['price'])

                    

        return redirect(checkout_session.url, code=303)
    except Exception as e:
         
         return JsonResponse({'error': str(e)}, status=400)



def success(request):
    return render(request, 'success')


def cancel(request):
    return render(request, 'cancel')