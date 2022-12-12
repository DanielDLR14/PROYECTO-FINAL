# Se crea la clase Clientes en donde iran los datos del mismo
class Clientes:
    # Se asigna una funcion init en donde iran establecidos los datos del cliente
    def __init__(self, nombre,apellido ,edad, telefono, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.cedula = cedula
        
    def __str__(self):
        return f"\nNombre = {self.nombre} {self.apellido} {self.edad} Tel: {self.telefono} Cedula: {self.cedula}"    

    def getnombre(self):
        
        return self.nombre
    def getapellido(self):
        return self.apellido

    def setnombre(self,nombre):
        self.nombre = nombre
    
    def setapellido(self,apellido):
        self.apellido = apellido


    def setedad(self,edad):
        self.edad = edad
    
    def settelefono(self,telefono):
        self.telefono = telefono
    
    def setcedula(self,cedula):
        self.cedula = cedula
# funcion para agregar datos 
def agregar():

    nombre = input("\nNombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    edad = int(input("Edad del cliente: "))
    telefono = int(input("Numero de telefono del cliente: "))
    cedula = int(input("Cedula del cliente: "))
    ClientesNuevos = Clientes(nombre, apellido, edad, telefono, cedula )
    ListaClientes.append(ClientesNuevos)
    
# funcion para mostrar datos obttenidos
def informar():
    
    print(" ")
    print("\n------Informe------")

    for num in range(0, len(ListaClientes)):
        print(f"{num + 1} - {ListaClientes[num]}")
# funcion para modificar datos y obtenidos
def modificar():
    informar()
    num = int(input("\nIntroduzca el numero de cliente que desea modificar: "))

    nombre = input("Introduzca un nuevo nombre: ")
    ListaClientes[num -1].setnombre(nombre)
    apellido = input("Introduzca un nuevo apellido: ")
    ListaClientes[num -1].setapellido(apellido)
    edad = int(input("Introduzca una nueva edad: "))
    ListaClientes[num -1].setedad(edad)
    telefono = int(input("Introduzca un nuevo numero telefonico: "))
    ListaClientes[num -1].settelefono(telefono)
    cedula = int(input("Introduzca una nueva cedula: "))
    ListaClientes[num -1].setcedula(cedula)
# funcion para poder borrar datos ya obtenidos
def borrar():
    informar()
    num = int(input("Ingrese el numero de cliente que desea borrar: "))
    print(f"¿Esta seguro/a de eliminar a {ListaClientes[num -1].getapellido() } {ListaClientes[num -1].getnombre()}?")
    respuesta = input("s- Borrar - n - No borrar\n> ")
    if respuesta == "s":
        ListaClientes.remove(ListaClientes[num -1])
    else:
        print("Cliente, no se ha borrado.")

ListaClientes = []
# funcion para mostrar apartado de opciones que querramos elegir
def submenu():
    opcion = ' '
    while(opcion != 'x'):
        print("\n-------- Clientes ---------")

        print("\n1- Agregar cliente")
        print("2- Modificar datos cliente")
        print("3- Datos sobre cliente")
        print("4- Borrar datos cliente")
        print("x- Salir de la seccion de Cliente")

        opcion = input("\nIngrese la opcion que desee: ")

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
    data = open("dataClientes.csv", "w")
    if len(ListaClientes) == 0:
        print("No hay data.")
        submenu()
    else:
        data.write("Nombre,APellido,Edad,Numero Telefono, Cedula\n")
        for num in range(0, len(ListaClientes)):
            data.write(f"{ListaClientes[num]},\n")
        print("\nData guardada exitosamente. Cierre para verificar.")
            