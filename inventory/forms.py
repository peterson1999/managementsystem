from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ('category', 'brand','name','price','stock')