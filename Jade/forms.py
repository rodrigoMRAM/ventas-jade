from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import *
from django.forms import ModelForm
from datetime import date

class FormularioDeVentas(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'
        # widgets = {
        #     'descripcion': forms.TextInput(attrs={
        #         'disabled': 'true'
        #     }) }


class FiltroPorFecha(forms.Form):
    fecha = forms.DateField(
        widget=forms.SelectDateWidget(),
        initial=date.today()  # Establece la fecha actual como valor inicial
    )