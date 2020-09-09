from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'layouts/index.html')

    def post(self, request):
        return render(request, 'layouts/login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'layouts/login.html')


class HomeView(View):
    def get(self, request):
        return render(request, 'layouts/home.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'layouts/register-employee.html')


class ProductRegisterView(View):
    def get(self, request):
        return render(request, 'layouts/register-product.html')


class EducationalBgView(View):
    def get(self, request):
        return render(request, 'layouts/educationalbg.html')


class TrainingView(View):
    def get(self, request):
        return render(request, 'layouts/training.html')
