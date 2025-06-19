from django import forms


class FormularioContacto(forms.Form):
    #Especificamos los campos del formulario
    asunto = forms.CharField(label='Asunto', max_length=100)
    emial = forms.EmailField(label='Email')
    mensaje = forms.CharField()

#Como podemos verlo
mi_formulario = FormularioContacto()
# print(mi_formulario)
# print(mi_formulario.as_p())
# print(mi_formulario.as_ul)
# print(mi_formulario.as_div)
mi_formulario = FormularioContacto({'asunto': 'prueba', 'email': 'prueba@mail.com', 'mensaje': 'Hola reicito buen dia, que quiere desayunar?'})
mi_formulario.is_valid() #valida el formulario y devuelve un True o False
mi_formulario.cleaned_data #Devuelve un diccionario con los datos del formulario si es valido
