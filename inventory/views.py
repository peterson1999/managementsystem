from django.shortcuts import render
from django.views.generic import View
# Create your views here.


class ProductRegisterView(View):
    def get(self, request):
        return render(request, 'register-products.html')

    def post(self, request):
        return render(request, 'home.html')
