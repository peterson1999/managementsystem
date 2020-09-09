from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path('index', views.IndexView.as_view(), name="index_view"),
    path('login', views.LoginView.as_view(), name="login_view"),
    path('home', views.HomeView.as_view(), name="home_view"),
    path('register', views.RegisterView.as_view(), name="register_view"),
    path('product-register', views.ProductRegisterView.as_view(),
         name="product_register_view"),
    path('educbg', views.EducationalBgView.as_view(), name="educbg_view"),
    path('training', views.TrainingView.as_view(), name="training_view"),
]
