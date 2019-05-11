from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='authentication-login'),
    path('/register', views.register, name='authentication-register'),
]