from django.db import models
from django.utils import timezone
# Create your models here.


class Person(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    mName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()


class Customer(Person):
    regdate = models.DateField(default=timezone.now)

    class Meta:
        db_table = "Customer"


class Employee(Person):
    email = models.EmailField()
    password = models.CharField(max_length=50)
    maritalStatus = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    spouseName = models.CharField(max_length=50)
    spouseOcc = models.CharField(max_length=20)
    numberOfChildren = models.IntegerField()
    motherName = models.CharField(max_length=50)
    motherOcc = models.CharField(max_length=20)
    fatherName = models.CharField(max_length=50)
    fatherOcc = models.CharField(max_length=20)
    height = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)
    religion = models.CharField(max_length=50)

    class Meta:
        db_table = "Employee"
