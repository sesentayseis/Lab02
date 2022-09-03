from django.shortcuts import render

# Create your views here.
def index(request):
    
    context={
        'saludo':'CÁLCULO DEL VOLUMEN DE UN CILINDRO'
    }
    return render(request,'cilindro/cilindro.html',context)
def calcular(request):
    context={
        'titulo':"El volumen del cilindro ",
        'num1':request.POST['n1'],
        'num2':request.POST['n2'],
        'radio':(float(request.POST['n1'])/2),
        'respuesta':  3.1416*( (float(request.POST['n1'])/2) **2)*float(request.POST['n2'])

    }
    return render(request,'cilindro/respuesta.html',context)