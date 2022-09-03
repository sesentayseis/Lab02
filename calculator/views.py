from ast import Str
from ctypes.wintypes import INT
from tkinter.tix import INTEGER
from django.shortcuts import render

# Create your views here.
def index(request):
    
    context={
        'saludo':'Bienvenido a mi primera calculadora'
    }
    return render(request,'calculator/calculator.html',context)
def sumar(request):
    context={
        'titulo':"Respuesta de la Suma:",
        'num1':request.POST['n1'],
        'num2':request.POST['n2'],
        'respuesta':int(request.POST['n1'])+int(request.POST['n2'])

    }
    return render (request,'calculator/respuesta_suma.html',context)
def restar(request):
    context={
        'titulo':"Respuesta de la Resta:",
        'num1':request.POST['n1'],
        'num2':request.POST['n2'],
        'respuesta':int(request.POST['n1'])-int(request.POST['n2'])

    }
    return render (request,'calculator/respuesta_resta.html',context)
def multiplicar(request):
    context={
        'titulo':"Respuesta de la Multiplicacion:",
        'num1':request.POST['n1'],
        'num2':request.POST['n2'],
        'respuesta':int(request.POST['n1'])*int(request.POST['n2'])

    }
    return render (request,'calculator/respuesta_multi.html',context)
