# Mediante el uso de Programación Orientada a Objetos, desarrollar un pequeño sistema que permita el mantenimiento de las ventas de videojuegos de PowerGames.

# Indicaciones:

# El sistema debe tener un menú de opciones que permita la interacción con el mismo.
# El sistema debe realizar las 4 operaciones de un CRUD (Create, Read, Update, Delete) para las siguientes clases (modelos):
# Clientes.
# Videojuegos.
# Ventas.

# El sistema debe permitir la carga y la exportación de data a través de archivos .csv (para todos los modelos).
# El sistema debe tener una opción que permita generar un archivo .csv con los videojuegos cuyas ventas sean mayores a RD$500.00.
# Se deben controlar las excepciones (data basura) haciendo uso de try-except.


###### Agregar condicion para lo de modificacion de las clases

# Daniel Arturo De La Rosa 21-1799

# Import VideoJuegos. 
import Clientes
import VideoJuegos
import Ventas

# Retorna o opcion de videojuegos.
while True:
    print("""
================================
   Bienvenido/a a PowerGames!!
================================
""")

    opcion= input("""
1 - Menu registro de videojuegos
2 - Menu registro de clientes
3 - Menu apartado de ventas
4 - Guardar en csv
5 - Guardar en csv los mayores a 500 pesos en venta.
6 - Cerrar el programa.


Seleccione: """)

    # Submenu 3 opcion de 1
    if opcion == "1":
        VideoJuegos.submenu3()

# Submenu menu.
    elif opcion == '2':
        Clientes.submenu()

        # Submenu 2 menu.
    
    elif opcion == '3':
        Ventas.submenu2()
        
        # Devuelve el objeto del videojuego
    elif opcion == '4':
        print("1- videojuegos")
        print("2- clientes")
        print("3- ventas")
        while True:
            try:
                respuesta = int(input("¿De qué quieres exportar la data en csv? "))
                break
            except ValueError:
                print("Se espera un numero.")
                continue
            
            # Retorna el objeto CSV a la respuesta de video.
        if respuesta == 1:
            VideoJuegos.CSV()
        elif respuesta == 2:
            Clientes.CSV()
        elif respuesta == 3:
            Ventas.CSV()
            
            
            # Devuelve el nombre de repuestas que se espera en csv
    elif opcion == '5':
        print("1- videojuegos")
        print("2- ventas")
        while True:
            try:
                respuesta = int(input("¿De qué quieres exportar la data en csv? "))
                break
            except ValueError:
                print("Se espera un numero.")
                continue
            
        if respuesta == 1:
            VideoJuegos.CSVventasMayores()
        elif respuesta == 2:
            Ventas.CSVventasMayores()
    elif opcion == '6':
        break
        
    else:
        print("\nNo data basura")
        continue
    
    