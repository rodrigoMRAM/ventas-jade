from django.shortcuts import render
from .forms import FormularioDeVentas, FiltroPorFecha
from .models import Producto, Ventas
# Create your views here.

def inicio(request):
    return render(request, 'index.html')

# def ventas(request):
#     if request.method == "POST":
#         formulario = FormularioDeVentas(request.POST)
#         if formulario.isvalid():

def mostrar_producto(request):
    productos = Producto.objects.all()
    if request.method == "POST":
        formulario = FormularioDeVentas(request.POST)
        print(formulario)
        if formulario.is_valid:
            formulario.save()
            return render(request, 'listado.html', {"productos": productos, "formulario" : formulario})
    else:
        formulario = FormularioDeVentas()
    return render(request, 'listado.html', {"productos": productos, "formulario" : formulario})



def filtro_por_fecha(request):
    eventos = None  # Inicialmente, no hay eventos
    form = FiltroPorFecha(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        fecha_seleccionada = form.cleaned_data['fecha']
        eventos = Ventas.objects.filter(fecha=fecha_seleccionada)

    return render(request, 'filtro.html', {'form': form, 'eventos': eventos})