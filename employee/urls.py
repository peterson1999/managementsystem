from django.urls import path
from . import views

app_name = 'employee'
urlpatterns = [
    path('register', views.RegisterView.as_view(), name="register_view"),
    path('educbg', views.EducationalBgView.as_view(), name="educbg_view"),
    path('training', views.TrainingView.as_view(), name="training_view"),
]
