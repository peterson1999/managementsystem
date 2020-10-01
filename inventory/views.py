from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *

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
