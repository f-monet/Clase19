from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario

# Create your views here.
def curso(self):
    curso=Curso(nombre="Curso de Django", comision=12345)
    curso.save()
    texto=f"Curso:{curso.nombre} comision:{curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')   

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html') 

def cursos(request):
    return render(request, 'AppCoder/cursos.html') 

def entregables(request):
    return render(request, 'AppCoder/entregables.html') 

def cursosFormulario(request):

    if request.method == 'POST':

        miFormulario=CursoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion=miFormulario.cleaned_data
            curso=Curso(nombre=informacion['nombre'], comision=informacion['comision'])
            curso.save()
            return render(request, 'AppCoder/inicio.html')
    else:
        miFormulario=CursoFormulario()
    return render(request, 'AppCoder/cursosFormulario.html', {'formulario':miFormulario} )


        
        

   