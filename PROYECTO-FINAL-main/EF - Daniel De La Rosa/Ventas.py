import Clientes

class Ventas:

    def __init__(self, nombreCliente,nombreVideojuego, CategoriaVideoJuego, PlataformaVideoJuego, PrecioVideoJuego  ):
        self.nombreCliente = nombreCliente
        self.nombreVideojuego = nombreVideojuego
        self.CategoriaVideoJuego = CategoriaVideoJuego
        self.PlataformaVideoJuego = PlataformaVideoJuego
        self.PrecioVideoJuego = PrecioVideoJuego
       
    def __str__(self):

        return f"Juego = {self.nombreVideojuego} Categoria: {self.CategoriaVideoJuego} Plataforma: {self.PlataformaVideoJuego}  Precio: {self.PrecioVideoJuego}"    

    def getnombre(self):
        return self.nombreVideojuego
    def getcategoria(self):
        return self.CategoriaVideoJuego
    
    def setnombre(self,nombreVideoJuego):
        self.nombreVideoJuego = nombreVideoJuego

    def setcategoria(self,CategoriaVideoJuego):
        self.CategoriaVideoJuego = CategoriaVideoJuego
    
    def setPlataforma(self,PlataformaVideoJuego):
        self.PlataformaVideoJuego = PlataformaVideoJuego
    
    def setPrecio(self,PrecioVideoJuego):
        self.PrecioVideoJuego = PrecioVideoJuego

def agregar():

    nombreVideoJuego = input("Introduzca el nombre del videojuego: ")
    CategoriaVideoJuego = input("Introduzca la categoria del videojuego: ")
    PlataformaVideoJuego = input("Introduzca la plataforma del videojuego: ")
    PreciovideoJuego = int(input("Introduzca el precio del videojuego: "))
    JuegosNuevos = Ventas(nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego)
    ListaJuegos.append(JuegosNuevos)

def informar():
    print(" ")
    print("------Informe Juegos------")
    for num in range(0, len(ListaJuegos)):
        print(f"{num + 1} - {ListaJuegos[num]}")

def modificar():
    informar()

    num = int(input("Introduzca el numero de cliente que desea modificar: "))

    nombreVideoJuego = input("Introduzca un nuevo nombre de videojuego: ")
    ListaJuegos[num -1].setnombre(nombreVideoJuego)
    CategoriaVideoJuego = input("Introduzca una nueva categoria del juego: ")
    ListaJuegos[num -1].setcategoria(CategoriaVideoJuego)
    PlataformaVideoJuego = input("Introduzca una nueva plataforma del juego: ")
    ListaJuegos[num -1].setPlataforma(PlataformaVideoJuego)
    PrecioVideoJuego = int(input("Introduzca un nuevo precio del juego: "))
    ListaJuegos[num -1].setPrecio(PrecioVideoJuego)

def borrar():
    informar()
    num = int(input("Ingrese el videojuego que desee borrar: "))
    print(f"¿Esta seguro/a de eliminar el juego {ListaJuegos[num -1].getnombre() } {ListaJuegos[num -1].getnombreVideoJuego()}?")
    respuesta = input("S- Borrar - N - No borrar")
    if respuesta == "s":
        ListaJuegos.remove(ListaJuegos[num -1])

ListaJuegos = []

def submenu3():
    opcion = ' '
    while(opcion != 'x'):
        print("-------- Ventas ---------")
        print("1- Realizar venta de videojuegos")
        print("2- Modificar los datos de las ventas")
        print("3- Datos sobre las ventas")
        print("4- Borrar datos de las ventas")
        print("x- Salir de la seccion de videojuegos")

        opcion = input("Ingrese la opcion que desee: ")

        if opcion == "1":
            agregar()
        
        elif opcion == "2":
            modificar()

        elif opcion == "3":
            informar()

        elif opcion == "4":
            borrar()