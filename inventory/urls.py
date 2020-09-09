from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('product-register', views.ProductRegisterView.as_view(),
         name="product_register_view"),
]
