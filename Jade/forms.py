from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
from django.forms import ModelForm
from datetime import date

class FormularioDeVentas(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'

        def clean(self):
            cleaned_data = super().clean()
            direccion = cleaned_data.get("direccion")
            valor_personalizado = cleaned_data.get("direccion_personalizada")

            if direccion == 'Otros' and not valor_personalizado:
                self.add_error('direccion_personalizada', "Este campo es obligatorio si seleccionaste 'Otros'.")
        # widgets = {
        #     'descripcion': forms.TextInput(attrs={
        #         'disabled': 'true'
        #     }) }

class FormularioProductos(forms.ModelForm):
    class Meta:
        model= Producto
        fields = ["nombre" , "precio"]


class FiltroPorFecha(forms.Form):
    fecha = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial=date.today()  # Establece la fecha actual como valor inicial
    )