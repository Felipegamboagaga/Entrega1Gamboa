from django.shortcuts import render
from VYM.models import familia, Aficion, Experiencia
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
    return render(request, 'index.html')

def ingresar_info(request):
    try:
        nombreI = request.GET['Nombre']
        edadI = request.GET['Edad']
        persona = familia(nombre = nombreI, edad = edadI)
        persona.save()
        return render(request, 'ingresarDatos.html')
    except MultiValueDictKeyError:
        return render(request, 'ingresarDatos.html')

    


def ingresar_aficion(request):
    try:
        nombre_E = request.GET['NombreEquipo']
        trofeos = int(request.GET['Trofeos'])
        Afi = Aficion(nombre_equipo = nombre_E, campeonatos = trofeos)
        Afi.save()
        print(request.GET)
        return render(request, 'ingresarAficion.html')
    except MultiValueDictKeyError:
        return render(request, 'ingresarAficion.html')
    

def ingresar_experiencia(request):
    try:
        leng = request.GET['Lenguaje']
        exp = int(request.GET['Experiencia'])
        exper = Experiencia(Lenguaje = leng, tiempo = exp)
        exper.save()
        print(request.GET)
        return render(request, 'ingresarExperiencia.html')
    except MultiValueDictKeyError:
        return render(request, 'ingresarExperiencia.html')



def busqueda(request):
   return render(request, 'buscar.html')

def resultados(request):
    print(request.GET)
    query = request.GET['search']
    name = familia.objects.filter(nombre__icontains=query)
    
    return render(request, 'resultados.html', {'name': name})
    


