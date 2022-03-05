from informacion_clientes import *
from manejo_bodega import *
from sistema_envios import *

def main():  
    continuar1 = 's'                                         
    while continuar1 != "n":
        opcion_central = input('Menú CENTRAL\n(1) Ir a Clientes\n(2) Ir a Bodega\n(3) Ir a Envíos\n(4) Salir\nElige una opción:')
        if opcion_central =='1':
            menu_principal_C()
        elif opcion_central =='2':
            menu_principal_B()
        elif opcion_central =='3':
            envios()
        elif opcion_central =='4':
            exit() 
        else:
             print("!! Opcion incorrecta")
    continuar1 = input(" Continua en Menu CENTRAL s/n : ")

main()
 