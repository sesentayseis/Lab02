from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
   path('volumen del cilindro',views.calcular,name='calcular'),
   
]