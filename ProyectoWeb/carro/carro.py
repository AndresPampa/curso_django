from django.http import HttpRequest

class Carro:

    def __init__(self, request: HttpRequest) -> None:
        self.request = request #Peticion del usuario
        self.session = request.session #Sesion de carrito
        carro = self.session.get("carro")

        #Chequear si existe el carro o sino existe
        if not carro:
            carro = self.session["carro"] = {}

        self.carro = carro

    #El carro debe agregar productos
    def agregar(self, producto: dict) -> None:
        if str(producto.id) not in self.carro.keys():
            self.carro[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": str(producto.precio),
                "cantidad": 1,
                "imagen": producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(producto.id):
                    value["cantidad"] = value["cantidad"] + 1
                    value["precio"] = str(float(value["precio"]) + float(producto.precio))
                    break
        
        self.guardar_carro()

    #Guardar y actualziar sesion del carro
    def guardar_carro(self) -> None:
        self.session["carro"] = self.carro
        self.session.modified = True

    #Eliminar productos del carro
    def eliminar(self, producto: dict) -> None:
        producto.id = str(producto.id) #* Este paso me parece que esta al pedo
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro() #Actualizamos el carro(session)
    
    #restar unidades de un producto
    def restar_producto(self, producto: dict) -> None:
        for key, value in self.carro.items():
            if key == str(producto.id):
                value["cantidad"] = value["cantidad"] - 1
                value["precio"] = str(float(value["precio"]) - float(producto.precio))
                if value["cantidad"] < 1:
                    self.eliminar(producto)
                break

        self.guardar_carro()

    
    #Limpiar carro
    def limpiar_carro(self) -> None:
        self.session["carro"] = {}
        self.session.modified = True
