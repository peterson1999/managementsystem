from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields = ('category', 'brand','name','price','stock',)


class MultiImages(forms.ModelForm):
    class Meta:
        model=MultiImage
        fields = ('image',)

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields = ('employeeEmail',)


class OrderedProduct(forms.ModelForm):
    class Meta:
        model=OrderedProducts
        fields = ('productID','price','qty',)