from django import forms
from employee.models import Customer, Employee


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('fName', 'lName')


class LoginForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('email', 'password')
