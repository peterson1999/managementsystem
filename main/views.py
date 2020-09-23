from django.shortcuts import render
from django.views.generic import View
from employee.models import Customer
from inventory.models import Product
# Create your views here.


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        return render(request, 'login.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        return render(request, 'home.html')


class HomeView(View):
    def get(self, request):
        customers = Customer.objects.all()
        products = Product.objects.all()
        context = {
            'customers': customers, 
            'products': products
        }
        return render(request, 'home.html', context)

    def post(self, request):
        return render(request, 'register-employee.html')
