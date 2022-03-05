import random

# Base de datos

productos = ["vasos", "cucharas", "cuchillos", "tenedores"]

ciudades = {"arica": "largo", "iquique": "largo", "antofagasta": "largo", "atacama": "largo",
            "coquimbo": "corto", "valparaiso": "corto", "metropolitana": "corto", "Rancagua": "corto",
            "maule": "corto", "ñuble": "corto", "biobio": "corto", "araucania": "corto",
            "losrios": "largo", "loslagos": "largo", "aysen": "largo", "magallanes": "largo", "antartica": "largo"}

bodega_A = {}
bodega_B = {}
# genera stock aleatorio entre 1 y 500 unidades
stock_aleatorio = [random.randint(1, 500) for x in range(100)]

# concatena dos lista en un diccionario
bodega_central = dict(zip(productos, stock_aleatorio))          # Bodega Central.. crea stock aleatorio

# funciones
def envios():
    print(" Base aleatoria de stock")
    print(stock_aleatorio)
    print("Productos y stock en Bodega Central")
    print(bodega_central)
    print("")
    print("--- !!  Bienvenidos a nuestro SISTEMA DE ENVIOS de PACLIGRI Company.....!!")
    print("------------------------------------------------------------------------------")
    print("SISTEMA DE ENVIOS")
    print("")
    nombre_envio = input("Ingrese su nombre : ")
    print("............... !!! Muy buen dia ", nombre_envio)
    print(ciudades.keys())
    ciudad_envio = input("Ingrese la ciudad a enviar : ")
    print(productos)
    producto_envio = input("Ingrese el producto : ")
    cantidad_envio = input("Ingrese la cantidad a enviar que no exceda al stock : ")
    cantidad_envio = int(cantidad_envio)
    print("------------------------------------------------------------------------------")
    
    for i in ciudades:
        if ciudad_envio == i:
            if ciudades[i] == "largo":
                stock_bodegaB = cantidad_envio #CAMBIO
                print("---------------------------------------------------------------------------------------")
                print("Su envio sera enviado a : ", ciudad_envio, "son mas de 1000 kilometros de distancia")
                print("---------------------------------------------------------------------------------------")
                for i in bodega_B:
                    stock_bodegaB = stock_bodegaB + bodega_B[i]
                if stock_bodegaB >= 500:
                    print("..!!!!!  Bodega B a superado las 500 unidades... ")
                else:
                    bodega_B[producto_envio] = cantidad_envio           #Stock se va a bodega B por ciudad envio largo
                    print("-----------------------------------------------------------------------------------------")
                    print(" Su envio se encuentra ahora en Bodega Sucursal B, despachos a larga distancia")
                    print("La Bodega B, su stock es: ")
                    print(bodega_B)
                    print("-----------------------------------------------------------------------------------------")
                    bodega_central[producto_envio] = bodega_central[producto_envio] - cantidad_envio   #Descuenta el stock de bodega central 
                    print("-----------------------------------------------------------------------------------------")
                    print(" Stock Bodega Central es : ")
                    print(bodega_central)
                    print("-----------------------------------------------------------------------------------------")
               
            if ciudades[i] == "corto":
                stock_bodegaA = cantidad_envio #CAMBIO
                print("---------------------------------------------------------------------------------------")
                print("Su envio sera enviado a : ", ciudad_envio, "son menos de 1000 kilometros de distancia")
                print("---------------------------------------------------------------------------------------")
                for i in bodega_A:
                    stock_bodegaA = stock_bodegaA + bodega_A[i]
                if stock_bodegaA >= 500:
                    print("..!!!!!  Bodega A a superado las 500 unidades... ")
                else:
                    bodega_A[producto_envio] = cantidad_envio           #Stock se va a bodega A por ciudad envio corto
                    print("-----------------------------------------------------------------------------------------")
                    print(" Su envio se encuentra ahora en Bodega Sucursal A, despachos a corta distancia")
                    print("La Bodega A, su stock es: ")
                    print(bodega_A)
                    bodega_central[producto_envio] = bodega_central[producto_envio] - cantidad_envio    #Descuenta el stock de bodega central
                    print("-----------------------------------------------------------------------------------------")
                    print(" Stock Bodega Central es : ")
                    print(bodega_central)
                    print("-----------------------------------------------------------------------------------------")

