from django.urls import path
from . import views

urlpatterns = [
    path('patientsList/', views.patientsList, name='patientsList'),
    path(r'^editPatient/<str:patientName>/<int:age>/<str:gender>/<int:phone>/<int:patientId>/<str:email>/$',views.editPatient, name='editPatient'),
    path('updatePatientToDB/<int:patientId>/', views.updatePatientToDB, name='updatePatientToDB'),
]
