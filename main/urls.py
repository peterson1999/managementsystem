from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('index', views.IndexView.as_view(), name="index_view"),
    path('login', views.LoginView.as_view(), name="login_view"),
    path('home', views.HomeView.as_view(), name="home_view"),
]
