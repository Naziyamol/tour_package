from django.shortcuts import render,redirect
from .forms import PackageForm 
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
import datetime

# Create your views here.

def home(request):
    return render(request,"home.html")

def registerUser(request):
    return render(request,"registerUser.html")


def vendor_register(request):
    if request.method == 'POST':
        name = request.POST['vendor']
        org_name = request.POST['org_name']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('vendor_register')
       
        vendor=Vendor.objects.create(name=name,oname=org_name,email=email,mobile=mobile_number,password=password);
        vendor.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')

    return render(request, 'registerVendor.html')


def user_register(request):
    if request.method == 'POST': 
        uname = request.POST['uname']
        email = request.POST['email']
        mobile_number = request.POST['mobile_number']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return redirect('user_register')
       
        user=Customer.objects.create(name=uname,email=email,mobile=mobile_number,password=password);
        user.save()
        messages.success(request, 'Registration successful. Please log in.')
        return redirect('login')

    return render(request, 'registerUser.html')


def login(request):
    error_message=""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        if(user_type=='user'):
            try:
                data=Customer.objects.get(email=email,password=password)
                if data:
                    return render(request,'user.html',{'data':data})
                else:
                    error_message = "Invalid credentials. Please try again."
            except:
                messages.warning(request,'Please enter valid details!!!.......')

        if(user_type=='vendor'):
            try:
                data=Vendor.objects.get(email=email,password=password)
                if data:
                    return render(request,'vendor.html',{'data':data})
                else:
                    error_message = "Invalid credentials. Please try again."
            except:
                messages.warning(request,'Please enter valid details!!!.......')
        return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')



def add_package(request,vid):
    vendor = Vendor.objects.get(id=vid)
    if request.method == 'POST':     
        name=request.POST.get('name')
        desc = request.POST.get('desc')
        duration = request.POST.get('duration')
        image = request.FILES.get('image')
        destin = request.POST.get('destin')
        price = request.POST.get('price')      
        package = Package(vendor_id=vid,name=name,desc=desc,duration=duration,image=image, destin=destin, price=price)
        package.save() 
        return redirect('vendor',vid=vid)
    return render(request, 'add_pack.html',{'data':vendor})

def edit_package(request, pid,vid):
    data = Vendor.objects.get(id=vid)
    packages = Package.objects.get(pk=pid)
    context = {
        'vendor': data,
        'packages': packages,
    }
    if request.method == 'POST':
        packages.name = request.POST.get('name')
        packages.destin = request.POST.get('destination')
        packages.desc = request.POST.get('description')
        packages.price = request.POST.get('price')
        packages.availability = request.POST.get('availability')
        packages.save()
        return redirect('vendor',vid=vid)
  
    return render(request, 'edit_package.html', context)

def user(request,uid):
    user=Customer.objects.get(id=uid)
    return render(request,"user.html",{'data':user})

def contact(request):
    return render(request,"contact.html")

def delete_package(request, pid,vid):
    packages = Package.objects.get(pk=pid)
    packages.delete()
    return redirect('vendor',vid=vid)

def vendor(request,vid):
    data=Vendor.objects.get(id=vid)
    packages = Package.objects.filter(vendor_id=vid).all()
    booking=Booking.objects.filter(vendor_id=vid).all()
    context = {
        'vendor': data,
        'packages': packages,
        'booking':booking,
    }
    return render(request,"vendor.html", context)

def packages(request,uid):
    user=Customer.objects.get(id=uid)
    packages = Package.objects.all()
    context={
        'user':user,
        'packages':packages,
    }
    return render(request,"packages.html",context)

def details(request,uid,pid):
    details=Package.objects.get(id=pid)
    user=Customer.objects.get(id=uid)
    vendors=Vendor.objects.all()
    vendor=Vendor.objects.get(id=details.vendor.id)
    image=details.image.url
    context={
        'details':details,
        'user':user,
        'vendor':vendor,
        'image':image,
    }
    return render(request,"details.html",context)


# def booking(request,uid,vid,pid):
      
#     vendor=Vendor.objects.get(id=vid)
#     user=Customer.objects.get(id=uid)
#     package=Package.objects.get(id=pid)
#     context = {
#         'vendor': vendor,
#         'packages': package,
# 	    'user':user,
#         }
#     return render(request,"package_booking.html",context)

def user_details(request):
    user=Customer.objects.all()

    return render(request, "user_manage.html",{'users':user})

def vendor_details(request):
    vendor=Vendor.objects.all()

    return render(request, "vendor_manage.html",{'vendors':vendor})

def booking_details(request):
    bookings = Booking.objects.all()   
    
    return render(request, 'booking_manage.html', {'bookings': bookings})

def package_details(request):
    package=Package.objects.all()

    return render(request, "package_manage.html",{'packages':package})

import razorpay
from django.conf import settings
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt	

def booking(request,uid,vid,pid):
    vendor=Vendor.objects.get(id=vid)
    user=Customer.objects.get(id=uid)
    package=Package.objects.get(id=pid)
    context = {
        'vendor': vendor,
        'package': package,
	    'user':user,
        }
  
    if request.method == 'POST':             
        amount =int(request.POST.get('price'))*100 
      
         
        client = razorpay.Client(auth=('rzp_test_wnleZz1Zk9xzDF','waK12xnK4ieU48EHtC9ULeKd'))
        payment_data = {
            'amount': amount,
            'currency': 'INR',
            'receipt': 'receipt_order_123456',
            'payment_capture': 1  # Auto capture payment
        }
        order = client.order.create(data=payment_data)
        order_id=order['id']
        print(order)
        expiry_date=datetime.datetime.now()+datetime.timedelta(day=30)
        booking=Booking.objects.create(user=user,package=package,vendor=vendor,booking_date=datetime.datetime.now(),expiry_date=expiry_date)
        booking.save()
        context1={
            'amount':amount,
            'order':order,
            'booking':booking,
            'orderid':order_id,
            
        }
        
        return render(request,"package_booking.html",context1)
     
    return render(request, 'package_booking.html',context)
    
@csrf_exempt
def success(request):
    return render(request, 'success.html')

def adminview(request):
    return render(request, 'AdminDashboard.html')

def vendor_admin(request):
    vendors = Vendor.objects.all()
   
    
    return render(request, 'vendor_details.html', {'vendors': vendors})

def user_admin(request):
    users=Customer.objects.all()
    return render(request, 'user_details.html', {'users': users})

def booking_admin(request):
    bookings = Booking.objects.all()   
    
    return render(request, 'booking_details.html', {'bookings': bookings})

def package_admin(request):
    packages = Package.objects.all()
    return render(request, 'package_details.html', {'packages':packages})

def logout(request):
    return render(request,"home.html")

