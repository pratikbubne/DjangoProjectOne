from django.urls import path
from . import views

urlpatterns = [
    path('testsList/', views.testsList, name='testsList'),
    path('addTest/', views.addTest, name='addTest'),
    path('addTestToDB/', views.addTestToDB, name='addTestToDB'),
    path('editTest/<str:testName>/<int:price>/<int:testId>/', views.editTest, name='editTest'),
    path('updateTestToDB/<int:testId>', views.updateTestToDB, name='updateTestToDB'),
    path('deletetest/<str:testName>/<int:price>/<int:testId>/', views.deletetest , name='deletetest'),
    path('deleteTestFromDB/<int:testId>', views.deleteTestFromDB,name='deleteTestFromDB')
]
