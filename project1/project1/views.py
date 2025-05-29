from django.http import HttpResponse, HttpRequest

# Como declaro una vista en django: solamente creando una funncion
def saludo(request: HttpRequest) -> HttpResponse:

    return HttpResponse("Hola pa! esta es la primera vista de mi proyecto de Django!")


def despedida(request: HttpRequest) -> HttpResponse:
    return HttpResponse("chau pa! Vuelva Prontos!")