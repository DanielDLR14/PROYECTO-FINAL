#Se hace la clase de ventas
class Ventas:
    # se define la funcion init con las variables que utlizaremos
    def __init__(self, nombreCliente,nombreVideojuego, CategoriaVideoJuego, PlataformaVideoJuego, PrecioVideoJuego  ):
        self.nombreCliente = nombreCliente
        self.nombreVideojuego = nombreVideojuego
        self.CategoriaVideoJuego = CategoriaVideoJuego
        self.PlataformaVideoJuego = PlataformaVideoJuego
        self.PrecioVideoJuego = PrecioVideoJuego
    # se retorna los datos que hemos ingresado en forma organizada
    def __str__(self):
        return f"Nombre Cliente: {self.nombreCliente} Nombre Videojuego: {self.nombreVideojuego} Categoria: {self.CategoriaVideoJuego} Plataforma: {self.PlataformaVideoJuego}  Precio: {self.PrecioVideoJuego}"    
    # se utiliza para poder borar o modificar los datos
    def getnombreVideojuego(self):
        return self.nombreVideoJuego
    def getnombreCliente(self):
        return self.nombreClientes
    def getcategoria(self):
        return self.CategoriaVideoJuego
# se utiliza para poder borar o modificar los datos
    def setnombreVideojuegos(self,nombreVideoJuego):
        self.nombreVideoJuego = nombreVideoJuego
        
    def setnombreClientes(self, nombreClientes):
        self.nombreClientes = nombreClientes

    def setcategoria(self,CategoriaVideoJuego):
        self.CategoriaVideoJuego = CategoriaVideoJuego
    
    def setPlataforma(self,PlataformaVideoJuego):
        self.PlataformaVideoJuego = PlataformaVideoJuego
    
    def setPrecio(self,PrecioVideoJuego):
        self.PrecioVideoJuego = PrecioVideoJuego
# funcion para el apartado de arrglar las ventas definiendo las variables 
def agregar():
    global nombreCliente ,nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego
    nombreCliente = input("Introduzca el nombre del cliente: ")
    nombreVideoJuego = input("Introduzca el nombre del videojuego: ")
    CategoriaVideoJuego = input("Introduzca la categoria del videojuego: ")
    PlataformaVideoJuego = input("Introduzca la plataforma del videojuego: ")
    PreciovideoJuego = int(input("Introduzca el precio del videojuego: "))
    Ventasnuevas = Ventas(nombreCliente ,nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego)
    ListaVentas.append(Ventasnuevas)
    global cliente
    cliente = ListaVentas[0] 

# funcion donde mostrara el informe de las ventas
def informar():
    print(" ")
    print("\n------Informe Ventas------")
    for num in range(0, len(ListaVentas)):
        print(f"{num + 1} - {ListaVentas[num]}")
# funcion donde se modificara los atos obtenidos
def modificar():
    informar()
    num = int(input("Introduzca el numero de ventas que desea modificar: "))

    nombreCliente  = input("Introduzca un nuevo nombre de cliente: ")
    ListaVentas[num -1].setnombreClientes(nombreCliente)
    nombreVideoJuego = input("Introduzca un nuevo nombre de videojuego: ")
    ListaVentas[num -1].setnombreVideojuegos(nombreVideoJuego)
    CategoriaVideoJuego = input("Introduzca una nueva categoria del juego: ")
    ListaVentas[num -1].setcategoria(CategoriaVideoJuego)
    PlataformaVideoJuego = input("Introduzca una nueva plataforma del juego: ")
    ListaVentas[num -1].setPlataforma(PlataformaVideoJuego)
    while True:
        try:
            PrecioVideoJuego = int(input("Introduzca un nuevo precio del juego: "))
            ListaVentas[num -1].setPrecio(PrecioVideoJuego)
        except ValueError:
            print("No data basura.\n")
# funcion donde se borrara dato de la venta
def borrar():
    informar()
    list(cliente)
    num = int(input("Ingrese la venta que desee borrar: "))
    print(f"¿Esta seguro/a de eliminar la venta {cliente[0]}  {cliente[1]} {cliente[4]}?")
    while True:
        try:
            respuesta = int(input("1- Borrar - 2 - No borrar\n> "))
            if respuesta == 1:
                ListaVentas.remove(ListaVentas[num -1])
            elif respuesta == 2:
                print("De acuerdo, no se borró la venta.")
            else:
                print("Data basura.")
            break
        except ValueError:
            print("No data basura.\n")

ListaVentas = []
# funcion del menu de las partes a querer utlizar

def submenu2():
    opcion = ' '
    while(opcion != 'x'):
        print("\n-------- Ventas ---------")
        print("1- Agregar Venta")
        print("2- Modificar los datos de la venta")
        print("3- Datos sobre la venta")
        print("4- Borrar datos de la venta")
        print("x- Salir de la seccion de ventas")

        opcion = input("Ingrese la opcion que desee: ")

        if opcion == "1":
            agregar()
        
        elif opcion == "2":
            modificar()

        elif opcion == "3":
            informar()

        elif opcion == "4":
            borrar()
# funncion para obtener apartado csv para las venas etc
def CSV():
    print("Guardar data en csv.")
    data = open("dataVentas.csv", "w")
    if len(ListaVentas) == 0:
        print("No hay data.")
        submenu2()
    else:
        data.write("Nombre Cliente,Nombre Videojuego,Categoria,Plataforma,Precio\n")
        for num in range(0, len(ListaVentas)):
            data.write(f"{ListaVentas[num]},\n")
        print("\nData guardada exitosamente. Cierre para verificar.")
        # funcion para sacar las entas mayores a 500 para 
def CSVventasMayores():
    print("Guardar data mayores a 500 en csv.")
    data = open("dataMayoresVentasVideojuegos.csv", "w")
    if len(ListaVentas) == 0:
        print("No hay data.")
        submenu2()
    else:
        data.write("Nombre,Categoria,Plataforma,Precio\n")
        for num in range(0, len(ListaVentas)):
            videoJuPrecio = Ventas(nombreCliente ,nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego)
            if videoJuPrecio.PrecioVideoJuego >= 500:
                data.write(f"{ListaVentas[num]}\n")
            else:
                print("No hay data con videojuegos con su precio igual o mayor a RD$500.00")