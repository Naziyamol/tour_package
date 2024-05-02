from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact/',views.contact,name='contact'),
    path('login/', views.login, name='login'),
     path('logout/', views.logout, name='logout'),

    path('registerUser/', views.user_register, name='user_register'),
    path('user/<int:uid>/', views.user, name='user'),
    path('registerVendor/', views.vendor_register, name='vendor_register'),
    path('packages/<int:uid>', views.packages, name='packages'),
    path('booking/<int:uid>/<int:vid>/<int:pid>/', views.booking, name='booking'),
    path('details/<int:uid>/<int:pid>/', views.details, name='details'),
    # path('payment/<int:uid>/<int:vid>/<int:pid>/', views.payment, name='payment'),
    path('adminview/', views.adminview, name='adminview'),
    path('success/', views.success, name='success'),
    path('package_details/', views.package_details, name='package_details'),
    path('booking_details/', views.booking_details, name='booking_details'),
    path('user_details/', views.user_details, name='user_details'),
    path('vendor_details/', views.vendor_details, name='vendor_details'),
    path('success/', views.success, name='success'),
    path('vendor/<int:vid>/', views.vendor, name='vendor'),
    path('delete_package/<int:vid>/<int:pid>/', views.delete_package, name='delete_package'),
    path('edit_package/<int:vid>/<int:pid>/', views.edit_package, name='edit_package'),
    path('add_package/<int:vid>/', views.add_package, name='add_package'),
     
]