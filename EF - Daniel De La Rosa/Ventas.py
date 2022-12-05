

class Ventas:

    def __init__(self,Nombrejuego, PlataformaJuego, cantidad, precio):
        self.Nombrejuego = Nombrejuego
        self.cantidad = cantidad
        self.precio = precio
        self.PlataformaJuego = PlataformaJuego
    def __str__(self):
        return f"Juego = {self.Nombrejuego} Plataforma {self.PlataformaJuego} Cantidad: {self.cantidad}  Precio: {self.precio}"    

