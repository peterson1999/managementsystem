from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('register-products', views.ProductRegisterView.as_view(),
         name="register_products_view"),

    path('orderform', views.OrderFormView.as_view(),
         name="order_form_view"),
]
