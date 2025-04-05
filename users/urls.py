
from django.urls import path

from . import views

urlpatterns = [
    path('loginPage/', views.LoginPage,name='loginPage'),
    path('resetpassword/', views.reset_password,name='resetPass'),
    path('confirmPassword/<uidb64>/<token>/', views.confirm_password, name='confirmPass'),
    
]