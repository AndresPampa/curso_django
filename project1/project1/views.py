from django.http import HttpResponse, HttpRequest
from django.template import Template, Context
import datetime

# Como declaro una vista en django: solamente creando una funncion
def saludo(request: HttpRequest) -> HttpResponse:

    #Levantamos el archivo
    doc_externo = open('./project1/plantillas/primera-vista.html')
    #Lo leemos y creamos el template
    plt = Template(doc_externo.read())
    doc_externo.close() #Lo cerramos para no estar utilizando recursos

    #creamos el contexto
    ctx = Context()

    documento = plt.render(ctx)

    #Retornamos el render con el contexto
    return HttpResponse(documento)


def despedida(request: HttpRequest) -> HttpResponse:
    return HttpResponse("chau pa! Vuelva Prontos!")


# Toma la hora y fecha del servidor.. WARNING!
def dameFecha(request: HttpRequest) -> HttpResponse:
    fecha_actual = datetime.datetime.now()

    documento = f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1 style="font-family: sans-serif; text-align: center;;">Fecha y hora Actuales: <mark>{fecha_actual.strftime("%d-%M-%Y : %H:%m")}</mark><h1>
        </body>
        </html>
    """

    return HttpResponse(documento)

# Django utiliza el URL friendly para que indexen bien en los buscadores y ayuda al SEO

def calculaEdad(request: HttpRequest, anio: int, edad: int) -> HttpResponse:

    # edad_actual = 18
    periodo = anio - 2025 #Año actual
    edad_futura = edad + periodo

    documento = f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h1 style="font-family: sans-serif; text-align: center;">En el año {anio} tendras {edad_futura}</mark><h1>
        </body>
        </html>
    """

    return HttpResponse(documento)
