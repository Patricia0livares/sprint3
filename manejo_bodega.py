import random                                                   # Librerias
import time

# Base de datos
productos = ["vasos", "cucharas", "cuchillos", "tenedores"]     # Lista de productos
bodega = {}                                                     # Diccionario de Bodega generado por productos de lista y stock aleatorio
# genera stock aleatorio entre 300 y 500 unidades
# print(" Genera stock aleatorio entre 300 y 500 unidades")
stock_aleatorio = [random.randint(300, 500) for x in range(100)]

# concatena dos lista en un diccionario
bodega = dict(zip(productos, stock_aleatorio))                  # Proceso geenracion diccionario bodega, concatenando productos y stock aleatorio

# funciones
def sumar(bodega, producto_suma, cantidad_suma):                 # Funcion sumar recibe parametros y los retorna nuevas unidades por producto recepciona parametros, lista bodega, producto suma, cantidad_suma, retorna lista actualizada producto
    print("-------------------------------------------------------------------------------------------------")
    for i in bodega:
        if i == producto_suma:
            cantidad_agregar = cantidad_suma + bodega[i]
            cantidad_agregar = int(cantidad_agregar)
            bodega[i] = cantidad_agregar
            return(bodega, producto_suma, cantidad_suma)
    
    

def restar(bodega, producto_resta, cantidad_resta):             # Funcion disminuir recibe parametros y los retorna nuevas unidades por producto
    print("-------------------------------------------------------------------------------------------------")
    for i in bodega:
        if i == producto_resta:
            cantidad_disminuir = bodega[i] - cantidad_resta
            cantidad_disminuir = int(cantidad_disminuir)
            bodega[i] = cantidad_disminuir
            return(bodega, producto_resta, cantidad_resta)
    

def agregar(bodega, producto_agregar, cantidad_agregar):         # Funcion agregar recibe parametros y los retorna nuevos productos
    print("-------------------------------------------------------------------------------------------------")
    print("Ingreso de nuevos productos a bodega : ")
    bodega[producto_agregar] = cantidad_agregar
    return(bodega, producto_agregar, cantidad_agregar)
    

def eliminar(bodega, producto_eliminar):              # Funcion eliminar recepciona y retorna paramatros, quitar productos de bodega
    print("-------------------------------------------------------------------------------------------------")
    del bodega[producto_eliminar]
    return(bodega, producto_eliminar)
    
    
def mostrar_productos():                               # Funcion mostrar productos y su stock --- con desfase de 1 segundo
    print("-------------------------------------------------------------------------------------------------")
    print("Muestra lista de productos en tienda con desfase de 1 segundo : ")
    for key, value in bodega.items():
        print(key, value)
        time.sleep(1)

def verificar():                                        # Funcion verificar si un producto tiene menos de 400 unidades enviar alerta
    print("-------------------------------------------------------------------------------------------------")
    print("Muestra lista de productos con menos de 400 unidades : ")
    for i in bodega:
         if bodega[i] < 400:
            print("!!!!!... producto : ", i, "            tiene de stock : ", bodega[i], "          menos de 400 unidades")
           
def menu_principal_B():
    print(" Genera stock aleatorio entre 300 y 500 unidades")
    print(stock_aleatorio)
    print(bodega)
    continuar = "s"
    while continuar == "s":
        print("..... Menu Principal BODEGA.....")
        print(" 1.- Sumar unidades")
        print(" 2.- Disminuir unidades")
        print(" 3.- Agregar nuevos productos")
        print(" 4.- Eliminar productos")
        print(" 5.- Mostrar productos con tiempo 1 segundo")
        print(" 6.- Verificar producto menos 400 u")
        print(" 7.- Salir")
        opcion = input(" Ingrese su opcion : ")
        opcion = int(opcion)
        if opcion == 1:                                                     # Funcion sumar() traspasa y recepciona parametros 
            print("Lista de productos")
            print(productos)
            producto_suma = input("Ingrese producto : ")
            cantidad_suma = input("Ingrese cantidad a sumar : ")
            cantidad_suma = int(cantidad_suma)
            sumar(bodega, producto_suma, cantidad_suma)
            print("Lista actualizada suma")
            print(bodega)
        elif opcion == 2:                                                   # Funcion restar() traspasa y recepciona parametros 
            print("Lista de productos")
            print(productos)
            producto_resta = input("Ingrese producto : ")
            cantidad_resta = input("Ingrese cantidad a restar : ")
            cantidad_resta = int(cantidad_resta)
            restar(bodega, producto_resta, cantidad_resta)
            print("Lista actualizada resta")
            print(bodega)
        elif opcion == 3:                                                   # Funcion agregar() traspasa y recepciona parametros 
            print("Lista de productos")
            print(productos)
            producto_agregar = input("Ingrese nuevo producto agregar : ")
            cantidad_agregar = input("Ingrese cantidad agregar : ")
            cantidad_agregar = int(cantidad_agregar)
            agregar(bodega, producto_agregar, cantidad_agregar)
            print("Lista actualizada")
            print(bodega)
        elif opcion == 4:                                                   # Funcion eliminar() traspasa y recepciona parametros 
            print("Lista de productos")
            print(bodega.keys())
            producto_eliminar = input("Ingrese producto eliminar : ")
            eliminar(bodega, producto_eliminar)
            print("Lista actualizada")
            print(bodega)
        elif opcion == 5:
            mostrar_productos()                                              # Funcion mostrar() lista todos los productos de bodega
        elif opcion == 6:                                                    # Funcion verificar() lista productos con menos de 400 unidades de stock
            verificar()
        elif opcion == 7:                                                    # Funcion verificar() lista productos con menos de 400 unidades de stock
            print("Salir")
            break
        else:
             print("!! Opcion incorrecta")
        continuar = input(" Continua en Menu Principal BODEGA  s/n : ")


