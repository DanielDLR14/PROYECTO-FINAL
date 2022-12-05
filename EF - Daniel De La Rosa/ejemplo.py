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

import sys


while True:
    print("""
================================
   Bienvenido/a a PowerGames :)
================================
  
""")
    opcion= input("""

1 - Introducir un videojuego nuevo
2 - Realizar venta de un videojuego
3 - Mostrar informacion de ventas
4 - Borrar un artículo
5 - Borrar todos los artículos
6 - Salir del programa


Seleccione: """)
    if opcion== "1":
        nombre = input("Nombre del juego: ")
        precio = float(input("Precio del juego: "))
        cantidad_vendida = 0.0
        nombres.append(nombre)
        precios.append(precio)
        cantidades_vendidas.append(cantidad_vendida)

    elif opcion== "2":
        nombre_viedojuego = input("Nombre del videojuego que se vende: ")
        if nombre_viedojuego in nombres:
            cantidad = float(input("Cantidad vendida de videojuegos: "))
            indice = nombres.index(nombre_viedojuego)
            precio = precios[indice]
            cantidades_vendidas[indice] += cantidad
            print(
                f"Se vende(n) {cantidad} {nombre_viedojuego}. Total: {cantidad * precio}")
        else:
            print("El artículo no existe")

            
    elif opcion== "3":
        if len(nombres) <= 0:
            print("No hay artículos")
            continue
        # Los nombres de artículos
        viedojuego_mas_vendido = nombres[0]
        viedojuego_menos_vendido = nombres[0]
        viedojuego_con_mas_ingresos = nombres[0]
        viedojuego_con_menos_ingresos = nombres[0]
        # Pero también necesitamos el conteo. Simplemente los inicializamos en un elemento del arreglo
        mas_vendido = cantidades_vendidas[0]
        menos_vendido = cantidades_vendidas[0]
        con_mas_ingresos = cantidades_vendidas[0] * precios[0]
        con_menos_ingresos = cantidades_vendidas[0] * precios[0]
        print("+--------------------+----------+----------+----------+")
        print("|NOMBRE CLIENTE      |NOMBRE VIDEOJUEGO        |CANT.     |PRECIO    |IMPORTE   |")
        print("+--------------------+----------+----------+----------+")
        indice = 0
        total = 0
        while indice < len(nombres):
            nombre = nombres[indice]
            precio = precios[indice]
            cantidad_vendida = cantidades_vendidas[indice]
            importe = precio * cantidad_vendida
            print("|{:<20}|{:>10.2f}|{:>10.2f}|{:>10.2f}|".format(
                nombre, cantidad_vendida, precio, importe))
            print("+--------------------+----------+----------+----------+")
            if cantidad_vendida > mas_vendido:
                mas_vendido = cantidad_vendida
                viedojuego_mas_vendido = nombre
            if cantidad_vendida < menos_vendido:
                menos_vendido = cantidad_vendida
                viedojuego_menos_vendido = nombre
            if importe > con_mas_ingresos:
                con_mas_ingresos = importe
                viedojuego_con_mas_ingresos = nombre
            if importe < con_menos_ingresos:
                con_menos_ingresos = importe
                viedojuego_con_menos_ingresos = nombre
            total += importe
            indice += 1

        print(
            "|--------------------|----------|TOTAL:    |{:>10.2f}|".format(total))
        print("+--------------------+----------+----------+----------+")
        print(
            f"Artículo más vendido: {viedojuego_mas_vendido}, con {mas_vendido} unidades")
        print(
            f"Artículo menos vendido: {viedojuego_menos_vendido}, con {menos_vendido} unidades")
        print(
            f"Artículo con más ingresos: {viedojuego_con_mas_ingresos}, con {con_mas_ingresos} euros")
        print(
            f"Artículo con menos ingresos: {viedojuego_con_menos_ingresos}, con {con_menos_ingresos} euros")
    elif opcion== "4":
        nombre_viedojuego = input("Nombre del artículo que se elimina: ")
        if nombre_viedojuego in nombres:
            indice = nombres.index(nombre_viedojuego)
            del nombres[indice]
            del precios[indice]
            del cantidades_vendidas[indice]
            print(f"Se elimina {nombre_viedojuego}")
        else:
            print("El artículo no existe")

    elif opcion== "5":
        if input("Seguro (s/n): ") == "s":
            nombres = []
            precios = []
            cantidades_vendidas = []

    elif opcion== "6":
        if input("Seguro (s/n): ") == "s":
            sys.exit()
