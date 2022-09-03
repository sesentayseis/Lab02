from django.urls import path

from . import views

urlpatterns = [
    path('', views.index,name='index'),
   path('respuesta_suma',views.sumar,name='sumar'),
   path('respuesta_resta',views.restar,name='restar'),
path('respuesta_multiplicacion',views.multiplicar,name='multiplicar'),
]

