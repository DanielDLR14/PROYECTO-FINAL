#El código es una función que toma el nombre del videojuego y devuelve una cadena con información sobre el mismo.
class Videojuegos:
     
     # funcion init con las ariables a utlizar para este apartado
    def __init__(self, nombreVideojuego, CategoriaVideoJuego, PlataformaVideoJuego, PrecioVideoJuego):
        self.nombreVideoJuego = nombreVideojuego
        self.CategoriaVideoJuego = CategoriaVideoJuego
        self.PlataformaVideoJuego = PlataformaVideoJuego
        self.PrecioVideoJuego = PrecioVideoJuego
        # funcion dodne se mostrara los datos que vayamos obteniendo
    def __str__(self):
        return f"Nombre = {self.nombreVideoJuego} Categoria: {self.CategoriaVideoJuego} Plataforma: {self.PlataformaVideoJuego}  Precio: {self.PrecioVideoJuego}"    
 # funciones donde  se podra modificar los datos
    def getnombre(self):
        return self.nombreVideoJuego
    def getcategoria(self):
        return self.CategoriaVideoJuego
    
    def getprecio(self):
        return self.PrecioVideoJuego

    def setnombre(self,nombreVideoJuego):
        self.nombreVideoJuego = nombreVideoJuego

    def setcategoria(self,CategoriaVideoJuego):
        self.CategoriaVideoJuego = CategoriaVideoJuego
    
    def setPlataforma(self,PlataformaVideoJuego):
        self.PlataformaVideoJuego = PlataformaVideoJuego
    
    def setPrecio(self,PrecioVideoJuego):
        self.PrecioVideoJuego = PrecioVideoJuego
# La primera línea es donde definimos nuestra función, que se llama "agregar".
#  Vamos a usar esta función para devolver información sobre el videojuego que se le pasó.  
def agregar():
    global nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego
    nombreVideoJuego = input("Introduzca el nombre del videojuego: ")
    CategoriaVideoJuego = input("Introduzca la categoria del videojuego: ")
    PlataformaVideoJuego = input("Introduzca la plataforma del videojuego: ")
    PreciovideoJuego = int(input("Introduzca el precio del videojuego: "))
    JuegosNuevos = Videojuegos(nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego)
    ListaJuegos.append(JuegosNuevos)
    print(ListaJuegos)
# funcion donde podras mostrar los datos recolectados
def informar():
    print(" ")
    print("\n------Informe Juegos------")
    for num in range(0, len(ListaJuegos)):
        print(f"{num + 1} - {ListaJuegos[num]}")
# funcion donde se podra modifiar los datos que vayamos a tener
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
    
# funcion para borrar datos que queramos
def borrar():
    informar()
    num = int(input("Ingrese el videojuego que desee borrar: "))
    print(f"¿Esta seguro/a de eliminar el juego {ListaJuegos[num -1].getnombre() } {ListaJuegos[num -1].getnombreVideoJuego()}?")
    respuesta = input("S- Borrar - N - No borrar")
    if respuesta == "s":
        ListaJuegos.remove(ListaJuegos[num -1])

ListaJuegos = []
# menu de las opciones que querramos realizar
def submenu3():
    opcion = ' '
    while(opcion != 'x'):
        print("\n-------- Juegos ---------")
        print("1- Agregar videojuego")
        print("2- Modificar los datos del videojuego")
        print("3- Datos sobre el videojuego")
        print("4- Borrar datos del videojuego")
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
    
def CSV():
    print("Guardar data en csv.")
    data = open("dataVideojuegos.csv", "w")
    if len(ListaJuegos) == 0:
        print("No hay data.")
        submenu3()
    else:
        data.write("Nombre,Categoria,Plataforma,Precio\n")
        for num in range(0, len(ListaJuegos)):
            data.write(f"{ListaJuegos[num]}\n")
        print("\nData guardada exitosamente. Cierre para verificar.")
        
def CSVventasMayores():
    print("Guardar data mayores a 500 en csv.")
    data = open("dataMayoresVentasVideojuegos.csv", "w")
    if len(ListaJuegos) == 0:
        print("No hay data.")
        submenu3()
    else:
        data.write("Nombre,Categoria,Plataforma,Precio\n")
        for num in range(0, len(ListaJuegos)):
            videoJuPrecio = Videojuegos(nombreVideoJuego, CategoriaVideoJuego, PlataformaVideoJuego, PreciovideoJuego)
            print(videoJuPrecio.PreciovideoJuego)
            if videoJuPrecio.getprecio() >= 500:
                data.write(f"{ListaJuegos[num]}\n")
            else:
                print("No hay data con videojuegos con su precio igual o mayor a RD$500.00")
