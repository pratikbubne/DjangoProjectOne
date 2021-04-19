from django.urls import path
from . import views

urlpatterns = [
    path('visitList/', views.visitList, name='visitList'),
    path('addVisit/', views.addVisit, name='addVisit'),
    path('addVisitToDB/', views.addVisitToDB, name='addVisitToDB'),
    path('ajaxLoadPatientEmail/', views.loadPatientEmail, name='ajaxLoadPatientEmail')
]
