from django import forms
from soccer.models import Cancha, Equipo, Jugador

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = ['nombre', 'descripcion', 'ciudad', 'creador_id', 'imagen_equipo']  # Incluye los campos que deseas mostrar en el formulario

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = ['nombre', 'correo', 'telefono', 'posicion', 'nivel', 'ciudad', 'imagen_jugador']  # Incluye los campos que deseas mostrar en el formulario

class CanchaForm(forms.ModelForm):
    class Meta:
        model = Cancha
        fields = ['nombre', 'direccion', 'ciudad', 'barrio', 'tipo', 'imagen_cancha']  # Incluye los campos que deseas mostrar en el formulario        