from django.shortcuts import render
from django.views.generic import View
from employee.models import Customer
from inventory.models import Product
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *
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
        print('update profile button clicked')
        if request.method == 'POST':	
           if 'btnUpdate' in request.POST:	
                print('update profile button clicked')
                category = request.POST.get("category")
                brand = request.POST.get("brand")
                name = request.POST.get("name")
                price = request.POST.get("price")
                stock = request.POST.get("stock")
                product_id=request.POST.get("id")
                image = request.FILES["image"]
                # email = request.POST.get("student-email")
                # phone = request.POST.get("student-phone")
                update_inventory = Product.objects.filter(id=product_id).update(category = category, brand=brand,name=name, price=price,stock=stock,image=image)
                print(update_inventory)
                print('profile updated')
           elif 'btnDelete' in request.POST:	
                print('delete button clicked')
                product_id = request.POST.get("id")
                stud = Product.objects.filter(id=product_id).delete()
                print('recorded deleted')
        return HttpResponse ('post')
