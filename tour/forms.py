# forms.py

from django import forms
from .models import Package

class PackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = ['name','destin','desc', 'price', 'availability']
