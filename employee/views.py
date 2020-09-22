from django.shortcuts import render
from django.views.generic import View
from .forms import Employee, EmployeeForm
from django.http import HttpResponse

# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'register-employee.html')

    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            fName = request.POST.get("fName")
            mName = request.POST.get("mName")
            lName = request.POST.get("lName")
            email = request.POST.get("email")
            password = request.POST.get("password")
            address = request.POST.get("address1") + " " + request.POST.get("address2") + " " + request.POST.get(
                "city") + ", " + request.POST.get("province") + ", " + request.POST.get("zip")
            birthdate = request.POST.get("birthdate")
            marStatus = request.POST.get("marStatus")
            gender = request.POST.get("gender")
            spouseName = request.POST.get("spouseFName") + " " + request.POST.get(
                "spouseMName") + " " + request.POST.get("spouseLName")
            spouseOcc = request.POST.get("spouseOcc")
            numOfChildren = request.POST.get("numOfChildren")
            motherName = request.POST.get("motherFName") + " " + request.POST.get(
                "motherMName") + " " + request.POST.get("motherLName")
            motherOcc = request.POST.get("motherOcc")
            fatherName = request.POST.get("fatherFName") + " " + request.POST.get(
                "fatherMName") + " " + request.POST.get("fatherLName")
            fatherOcc = request.POST.get("fatherOcc")
            height = request.POST.get("height")
            weight = request.POST.get("weight")
            religion = request.POST.get("religion")
            form = Employee(fName=fName, lName=lName, mName=mName, address=address, birthdate=birthdate, email=email, password=password, maritalStatus=marStatus, gender=gender, spouseName=spouseName, spouseOcc=spouseOcc,
                            numberOfChildren=numOfChildren, motherName=motherName, motherOcc=motherOcc, fatherName=fatherName, fatherOcc=fatherOcc, height=height, weight=weight, religion=religion)
            form.save()
            return HttpResponse('Successfully Registered!')
        else:
            print(form.errors)
            return HttpResponse("Not Valid!")


class EducationalBgView(View):
    def get(self, request):
        return render(request, 'educationalbg.html')

    def post(self, request):
        return render(request, 'training.html')


class TrainingView(View):
    def get(self, request):
        return render(request, 'training.html')

    def post(self, request):
        return render(request, 'home.html')
