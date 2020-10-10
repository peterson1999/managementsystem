from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.db.models import Sum
from employee.models import Customer, Person
from inventory.models import Product, MultiImage
from .models import *
from .forms import CustomerForm
from inventory.forms import ProductForm
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
        images = MultiImage.objects.all()
        items = products.count()
        enddate = datetime.today()
        startdate = enddate - timedelta(days=6)
        purchase = Customer.objects.filter(
            regdate__range=[startdate, enddate]).count()
        qty = Product.objects.aggregate(Sum('stock'))
        value = Product.objects.aggregate(Sum('price'))

        context = {
            'customers': customers,
            'products': products,
            'images': images,
            'item_summary': items,
            'purchase_summary': purchase,
            'qty_summary': qty,
            'value_summary': value
        }
        return render(request, 'home.html', context)

    def post(self, request):
        print('update profile button clicked')
        if request.method == 'POST':
            # Customer
            if 'addCustomer' in request.POST:
                form = CustomerForm(request.POST)
                if form.is_valid():
                    fName = request.POST.get("fName")
                    mName = request.POST.get("mName")
                    lName = request.POST.get("lName")
                    address = request.POST.get("address")
                    birthdate = request.POST.get("birthdate")
                    form = Customer(
                        fName=fName, lName=lName, mName=mName, address=address, birthdate=birthdate)
                    form.save()
                else:
                    print(form.errors)
                    return HttpResponse("Error in Adding Customer")
            elif 'updateCustomer' in request.POST:
                customer_id = request.POST.get("id")
                print(customer_id)
                customer_fName = request.POST.get("fName")
                customer_mName = request.POST.get("mName")
                customer_lName = request.POST.get("lName")
                customer_bday = request.POST.get("bday")
                customer_address = request.POST.get("address")
                update_customer = Person.objects.filter(id=customer_id).update(
                    fName=customer_fName, lName=customer_lName, mName=customer_mName, address=customer_address, birthdate=customer_bday)
            elif 'deleteCustomer' in request.POST:
                customer_id = request.POST.get("id")
                delete_customer = Customer.objects.filter(
                    person_ptr_id=customer_id).delete()
                delete_person = Person.objects.filter(id=customer_id).delete()

            # Product
            elif 'btnUpdate' in request.POST:
                print('update profile button clicked')
                category = request.POST.get("category")
                brand = request.POST.get("brand")
                name = request.POST.get("name")
                price = request.POST.get("price")
                stock = request.POST.get("stock")
                product_id = request.POST.get("id")
                image = request.FILES.getlist("image")

                update_inventory = Product.objects.get(id=product_id)
                update_image = MultiImage.objects.filter(
                    product_id_id=product_id)
                dbImgCount = len(update_image)
                imageCount = len(image)
                if (imageCount > 0):
                    if (dbImgCount >= imageCount):
                        for i in range(dbImgCount):
                            update_image1 = MultiImage.objects.get(
                                id=update_image[i].id)
                            try:
                                update_image1.image = image[i]
                            except IndexError:
                                update_image1.image = None
                            update_image1.save()
                    else:
                        for i in range(imageCount):
                            try:
                                update_image1 = MultiImage.objects.get(
                                    id=update_image[i].id)
                                update_image1.image = image[i]
                                update_image1.save()
                            except IndexError:
                                formImage = MultiImage(
                                    product_id=update_inventory, image=image[i])
                                formImage.save()

                update_inventory.category = category
                update_inventory.brand = brand
                update_inventory.name = name
                update_inventory.price = price
                update_inventory.stock = stock
                update_inventory.save()

                print(update_inventory)
                print('profile updated')
            elif 'btnDelete' in request.POST:
                print('delete button clicked')
                product_id = request.POST.get("id")
                stud = Product.objects.filter(id=product_id).delete()
                print('recorded deleted')
        return redirect('main:home_view')
