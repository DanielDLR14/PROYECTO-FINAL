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
        return f"Nombre = {self.nombre} {self.apellido} {self.edad} Tel: {self.telefono} Cedula: {self.cedula}"    

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

def agregar():

    nombre = input("Nombre del cliente: ")
    apellido = input("Apellido del cliente: ")
    edad = int(input("Edad del cliente: "))
    telefono = int(input("Numero de telefono del cliente: "))
    cedula = int(input("Cedula del cliente: "))
    ClientesNuevos = Clientes(nombre, apellido, edad, telefono, cedula )
    ListaClientes.append(ClientesNuevos)

def informar():
    
    print(" ")
    print("------Informe------")

    for num in range(0, len(ListaClientes)):
        print(f"{num + 1} - {ListaClientes[num]}")

def modificar():
    informar()
    num = int(input("Introduzca el numero de cliente que desea modificar: "))

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

def borrar():
    informar()
    num = int(input("Ingrese el numero de cliente que desea borrar: "))
    print(f"¿Esta seguro/a de eliminar a {ListaClientes[num -1].getapellido() } {ListaClientes[num -1].getnombre()}?")
    respuesta = input("S- Borrar - N - No borrar")
    if respuesta == "s":
        ListaClientes.remove(ListaClientes[num -1])

ListaClientes = []

def submenu():
    opcion = ' '
    while(opcion != 'x'):
        print("\n-------- Clientes ---------")

        print("1- Agregar cliente")
        print("2- Modificar datos cliente")
        print("3- Datos sobre cliente")
        print("4- Borrar datos cliente")
        print("x- Salir de la seccion de Cliente")

        opcion = input("Ingrese la opcion que desee: ")

        if opcion == "1":
            agregar()
        
        elif opcion == "2":
            modificar()

        elif opcion == "3":
            informar()

        elif opcion == "4":
            borrar()


    


