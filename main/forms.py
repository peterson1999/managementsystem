from django import forms
from employee.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fName', 'lName')
