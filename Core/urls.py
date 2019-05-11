from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.core, name='Core-core'),
]