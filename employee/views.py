from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Employee, EmployeeForm
from django.http import HttpResponse
from datetime import date

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
            # Educational Background
            elemSchoolName = request.POST.get("elemSchoolName")
            elemGrade = request.POST.get("elemGrade")
            elemDateCompleted = request.POST.get("elemDateCompleted")
            if elemDateCompleted == "":
                elemDateCompleted = date(1111, 11, 11)
            elemAwards = request.POST.get("elemAwards")
            jhsSchoolName = request.POST.get("jhsSchoolName")
            jhsGrade = request.POST.get("jhsGrade")
            jhsDateCompleted = request.POST.get("jhsDateCompleted")
            if jhsDateCompleted == "":
                jhsDateCompleted = date(1111, 11, 11)
            jhsAwards = request.POST.get("jhsAwards")
            shsSchoolName = request.POST.get("shsSchoolName")
            shsGrade = request.POST.get("shsGrade")
            shsDateCompleted = request.POST.get("shsDateCompleted")
            if shsDateCompleted == "":
                shsDateCompleted = date(1111, 11, 11)
            shsAwards = request.POST.get("shsAwards")
            shsStrand = request.POST.get("shsStrand")
            collegeSchoolName = request.POST.get("collegeSchoolName")
            collegeCourse = request.POST.get("collegeCourse")
            collegeLvl = request.POST.get("collegeLvl")
            if collegeLvl == "":
                collegeLvl = 0
            collegeDateCompleted = request.POST.get("collegeDateCompleted")
            if collegeDateCompleted == "":
                collegeDateCompleted = date(1111, 11, 11)
            collegeAwards = request.POST.get("collegeAwards")
            postgradSchoolName = request.POST.get("postgradSchoolName")
            postgradCourse = request.POST.get("postgradCourse")
            postgradLvl = request.POST.get("postgradLvl")
            if postgradLvl == "":
                postgradLvl = 0
            postgradDateCompleted = request.POST.get("postgradDateCompleted")
            if postgradDateCompleted == "":
                postgradDateCompleted = date(1111, 11, 11)
            postgradAwards = request.POST.get("postgradAwards")
            # Training
            trainingTitle = request.POST.get("trainTitle")
            trainingSponsor = request.POST.get("trainSponsors")
            trainingDate = request.POST.get("trainDate")
            if trainingDate == "":
                trainingDate = date(1111, 11, 11)

            form = Employee(fName=fName, lName=lName, mName=mName, address=address, birthdate=birthdate, email=email, password=password, maritalStatus=marStatus, gender=gender, spouseName=spouseName, spouseOcc=spouseOcc,
                            numberOfChildren=numOfChildren, motherName=motherName, motherOcc=motherOcc, fatherName=fatherName, fatherOcc=fatherOcc, height=height, weight=weight, religion=religion,
                            elemSchoolName=elemSchoolName, elemGrade=elemGrade, elemDateCompleted=elemDateCompleted, elemAwards=elemAwards, jhsSchoolName=jhsSchoolName, jhsGrade=jhsGrade, jhsDateCompleted=jhsDateCompleted, jhsAwards=jhsAwards,
                            shsSchoolName=shsSchoolName, shsGrade=shsGrade, shsDateCompleted=shsDateCompleted, shsAwards=shsAwards, shsStrand=shsStrand,
                            collegeSchoolName=collegeSchoolName, collegeCourse=collegeCourse, collegeLvl=collegeLvl, collegeDateCompleted=collegeDateCompleted, collegeAwards=collegeAwards,
                            postgradSchoolName=postgradSchoolName, postgradCourse=postgradCourse, postgradLvl=postgradLvl, postgradDateCompleted=postgradDateCompleted, postgradAwards=postgradAwards,
                            trainTitle=trainingTitle, trainSponsors=trainingSponsor, trainDate=trainingDate)
            form.save()
            return redirect('main:home_view')
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
