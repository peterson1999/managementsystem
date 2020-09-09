from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class RegisterView(View):
    def get(self, request):
        return render(request, 'register-employee.html')

    def post(self, request):
        return render(request, 'educationalbg.html')


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
