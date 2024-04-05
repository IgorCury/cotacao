from django.contrib import admin
from django.urls import path, include
from . import views
from .views import cot_list, generate_pdf


urlpatterns = [
    path('', views.home, name='home'),
    path('cotacao', views.cotacao, name='cotacao'),
    path('formrec/', views.formrec, name='formrec'),
    path('update/<int:id>', views.update, name="update"),
    path('upate/updcot/<int:id>', views.updcot, name='updcot'),
    path('delete/<int:id>/', views.delete, name='delete'),
     path('core/generate-pdf/<int:id>/', views.generate_pdf, name='generate_pdf'),
    path('', cot_list, name='cot_list'),
]
