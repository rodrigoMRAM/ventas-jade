from django.shortcuts import redirect, render
from .forms import FormularioDeVentas, FiltroPorFecha , FormularioProductos
from .models import Producto, Ventas
from django.views.generic import UpdateView, DeleteView
from django.db.models import Sum
from django.urls import reverse_lazy
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
            return redirect("ultimo_producto")
            # return render(request, 'listado.html', {"productos": productos, "formulario" : formulario})
    else:
        formulario = FormularioDeVentas()
    return render(request, 'listado.html', {"productos": productos, "formulario" : formulario})



def filtro_por_fecha(request):
    form = FiltroPorFecha(request.POST or None)
    eventos = []  # Inicializamos como una lista vacía

    suma_precio = 0  # Inicializamos la suma

    if request.method == 'POST' and form.is_valid():
        fecha_seleccionada = form.cleaned_data['fecha']
        eventos = Ventas.objects.filter(fecha=fecha_seleccionada).order_by("-id")

        # Usamos aggregate para obtener la suma de 'total'
        suma_precio = eventos.aggregate(Sum('total'))['total__sum'] or 0  # Manejo de caso donde no hay eventos

    return render(request, 'filtro.html', {'form': form, 'eventos': eventos, 'suma_precio': suma_precio})
    # else:
    #     form = filtro_por_fecha()
    # return render(request, 'filtro.html', {'form': form})


class ProductoUpdate(UpdateView):
    model = Producto
    success_url = "/productos/"
    fields = ['nombre', 'precio']


def agregar_producto(request):
    productos = Producto.objects.all()
    if request.method == "POST":
        formulario = FormularioProductos(request.POST)
        print(formulario)
        if formulario.is_valid:
            formulario.save()
            return redirect("productos")
            # return render(request, 'listado.html', {"productos": productos, "formulario" : formulario})
    else:
        formulario = FormularioProductos()
    return render(request, 'addProduct.html', {"productos": productos, "formulario" : formulario})

class EliminarProducto(DeleteView):
    model = Producto 
    success_url = reverse_lazy('editar')

def ultimo_producto(request):
    producto = Ventas.objects.latest('id')
    return render(request, "ultimoProducto.html" ,{"producto" : producto})