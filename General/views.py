from django.shortcuts import render

def inicio(request):
    
    context={
        
    }
    return render(request,"index.html",context)

def sedes(request):
    return render(request, "sedes.html")

def servicios(request):
    return render(request, "servicios.html")

def clinica1(request):
    return render(request, "clinica1.html")

def clinica2(request):
    return render(request, "clinica2.html")

def clinica3(request):
    return render(request, "clinica3.html")

def politica(request):
    return render(request, "politica.html")


def certificacion(request):
    return render(request, "certificacion.html")

def notas(request):
    return render(request, "notas.html")