from django.db import models
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=30, null=False)
    mobile = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)

class AdminLogin(models.Model):
    username = models.CharField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)

class Vendor(models.Model):
    oname = models.CharField(max_length=30, null=False)
    name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=30, null=False)
    mobile = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=20, null=False)


class Package(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    destin = models.CharField(max_length=100, null=False)
    price = models.CharField(max_length=25)
    availability = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    image=models.ImageField(upload_to='gallery/',default=None)
    duration=models.IntegerField(null=False,default=0)


class Booking(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    status=models.CharField(max_length=100,default="pending")
