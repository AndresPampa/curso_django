from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=50, required=True)
    email = forms.CharField(label='Email', max_length=50, required=True)
    contenido = forms.CharField(label='Contenido', max_length=200, widget=forms.Textarea)