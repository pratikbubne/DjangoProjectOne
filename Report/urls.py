from django.urls import path
from . import views

urlpatterns = [
    path('reportsList/', views.reportsList, name='reportsList'),
    path('addReport/', views.addReport, name='addReport'),
    path('addReportToDB/', views.addReportToDB, name='addReportToDB'),
    path('ajaxLoadPatientData/', views.loadPatientData, name='ajaxLoadPatientData'),
    path('displayreport/<int:reportId>/', views.displayreport, name='displayreport')
]
