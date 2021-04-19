from django.urls import path
from . import views

urlpatterns = [
    path('addoffer/', views.addoffer, name='addoffer')
    ]