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

# Daniel Arturo De La Rosa 21-1799

import Clientes
import VideoJuegos


while True:
    print("""
================================
   Bienvenido/a a PowerGames!!
================================
  
""")

    opcion= input("""

1 - Menu registro de videojuegos
2 - Menu Venta y registro de cliente
3 - Mostrar informacion de ventas
4 - Salir del programa


Seleccione: """)

    if opcion == "1":
        VideoJuegos.submenu2()
