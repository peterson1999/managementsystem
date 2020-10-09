from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *
from employee.models import Employee
from employee.models import Customer, Person
from inventory.models import Product, MultiImage
from .models import *
from main.forms import CustomerForm
from .forms import ProductForm
from employee.forms import EmployeeForm


# Create your views here.


class ProductRegisterView(View):
    def get(self, request):
        return render(request, 'register-products.html')

    def post(self, request):
        form1 = MultiImages(request.POST, request.FILES)
        form = ProductForm(request.POST)

        if (form.is_valid() and form1.is_valid()):

            category = request.POST.get("category")
            brand = request.POST.get("brand")
            name = request.POST.get("name")
            price = request.POST.get("price")
            stock = request.POST.get("stock")

            form = Product(category=category, brand=brand,
                           name=name, price=price, stock=stock)

            form.save()
            for file in request.FILES.getlist("image"):
                form1 = MultiImage(product_id=form, image=file)
                form1.save()
            return redirect('main:home_view')

        else:
            print(form.errors)
            return HttpResponse('not valid')

class OrderFormView(View):
    def get(self, request):
        customers = Customer.objects.all()
        products = Product.objects.all()
        images = MultiImage.objects.all()
        employees = Employee.objects.all()
        context = {
            'customers': customers,
            'products': products,
            'images':images,
            'employees':employees
         }
        return render(request, 'orderform.html', context)
    def post(self, request):
        form = OrderForm(request.POST)
        form1 = OrderedProduct(request.POST)

        # if (form.is_valid() and form1.is_valid()):
        customerdetails= request.POST.get("customerdetails")
        
        customerID = int (customerdetails.split(' ',1)[0]) 
        
        
        employeeEmail = request.POST.get("employeeEmail")
        
        
        form = Order(customerID=customerID, employeeEmail=employeeEmail)

        form.save()
        print("Dasdasdasda")
        productID = request.POST.getlist("productID")
        price = request.POST.getlist("price")
        qty = request.POST.getlist("qty")
        # for p in productID:
        #     form1 = OrderedProducts(productID=p,  order_id=form)
        # for s in price:
        #     form1 = OrderedProducts(price=s, order_id=form)
        # for q in qty:
        #     form1 = OrderedProducts(qty=q, order_id=form)
        #     form1.save()
        for i in range(len(productID)):
            if (qty[i]!='0'):
                form1 = OrderedProducts(productID=productID[i], price=price[i],qty=qty[i],order_id=form)
                form1.save()
        return redirect('main:home_view')

        # else:
        #     print(form.errors)
        #     return HttpResponse('not valid')