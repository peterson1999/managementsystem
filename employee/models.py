from django.db import models
from django.utils import timezone
# Create your models here.


class Person(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    mName = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    birthdate = models.DateField()
    isDeleted = models.BooleanField(default=False)

    class Meta:
        db_table = "Person"


class Customer(Person):
    customer_id = models.AutoField(primary_key=True)
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

    # Educational Background
    elemSchoolName = models.CharField(max_length=50, blank=True, null=True)
    elemGrade = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True, null=True)
    elemDateCompleted = models.DateField(default=None, blank=True, null=True)
    elemAwards = models.TextField(max_length=100, blank=True, null=True)
    jhsSchoolName = models.CharField(max_length=50, blank=True, null=True)
    jhsGrade = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True, null=True)
    jhsDateCompleted = models.DateField(default=None, blank=True, null=True)
    jhsAwards = models.TextField(max_length=100, blank=True, null=True)
    shsSchoolName = models.CharField(max_length=50, blank=True, null=True)
    shsGrade = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True, null=True)
    shsDateCompleted = models.DateField(default=None, blank=True, null=True)
    shsAwards = models.TextField(max_length=100, blank=True, null=True)
    shsStrand = models.CharField(max_length=5, blank=True, null=True)
    collegeSchoolName = models.CharField(max_length=50, blank=True, null=True)
    collegeCourse = models.CharField(max_length=50, blank=True, null=True)
    collegeLvl = models.IntegerField(blank=True, null=True)
    collegeDateCompleted = models.DateField(
        default=None, blank=True, null=True)
    collegeAwards = models.TextField(max_length=100, blank=True, null=True)
    postgradSchoolName = models.CharField(max_length=50, blank=True, null=True)
    postgradCourse = models.CharField(max_length=50, blank=True, null=True)
    postgradLvl = models.IntegerField(blank=True, null=True)
    postgradDateCompleted = models.DateField(
        default=None, blank=True, null=True)
    postgradAwards = models.TextField(max_length=100, blank=True, null=True)

    # Training
    trainTitle = models.CharField(max_length=50, blank=True, null=True)
    trainSponsors = models.CharField(max_length=50, blank=True, null=True)
    trainDate = models.DateField(default=None, blank=True, null=True)

    class Meta:
        db_table = "Employee"
