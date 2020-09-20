from django.shortcuts import render
from django.views.generic import View
from .forms import *
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.


class ProductRegisterView(View):
    def get(self, request):
        return render(request, 'register-products.html')

    def post(self, request):
        form = ProductForm(request.POST)

        if form.is_valid():
            
            category = request.POST.get("category")
            brand = request.POST.get("brand")
            name = request.POST.get("name")
            price = request.POST.get("price")
            stock = request.POST.get("stock")
            image = request.FILES["image"]
            form = Product(category = category, brand=brand,name=name, price=price,stock=stock, image=image)
            form.save()
            return HttpResponse ('Product Saved!')

        else:
            print(form.errors)
            return HttpResponse('not valid')
        # return render(request, 'home.html')
