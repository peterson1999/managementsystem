from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'address', 'birthdate', 'maritalStatus', 'gender', 'spouseName', 'spouseOcc',
                  'numberOfChildren', 'motherName', 'motherOcc', 'fatherName', 'fatherOcc', 'height', 'weight', 'religion')
