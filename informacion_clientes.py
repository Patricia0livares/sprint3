#Bases de datos
clientes = {"ID1010": ["patricia", "olivares", "17", "putaendo"],
            "ID1020": ["ignacio", "montero", "14", "perrito"],
            "ID1030": ["ricardo", "ponce", "12", "gatito"],
            "ID1040": ["claudio", "irarrazabal", "18", "gaviota"]}

# funciones
def agregar(clientes, id_cliente_agregar, nombre_cliente_agregar, apellido_cliente_agregar, edad_cliente_agregar, contraseña_cliente_agregar):  # Funcion agregar nuevos clientes traspasa y retorna parametros
    clientes[id_cliente_agregar] = [nombre_cliente_agregar, apellido_cliente_agregar, edad_cliente_agregar, contraseña_cliente_agregar]
    return(nombre_cliente_agregar, apellido_cliente_agregar, edad_cliente_agregar, contraseña_cliente_agregar)
   
def eliminar(clientes):                                             # Funcion eliminar clientes, traspasa y rotorna parametros
    print("Lista de Clientes : ")
    for i in clientes:
        print(i, clientes[i])
    cliente_eliminar = input("Ingrese ID, Cliente a eliminar : ")
    del clientes[cliente_eliminar]
    return(clientes)
       
def mostrar_clientes():                                              # Funcion mostrar lista de Clientes
    print("Lista de Clientes")
    for key, value in clientes.items():
        print(key, value)
           
def menu_principal_C():                                               # Funcion menu principal
    continuar2 = "s"
    while continuar2 == "s":
        print("..... Menu Principal CLIENTES.....")
        print(" 1.- Agregar Clientes")
        print(" 2.- Eliminar Clientes")
        print(" 3.- Mostrar Clientes")
        print(" 4.- Volver a Menu CENTRAL")
        opcion = input(" Ingrese su opcion : ")
        opcion = int(opcion)
        if opcion == 1:                                             # Funcion agregar(), traspasa y recepciona parametros
            print("Lista de Clientes")
            print(clientes)
            id_cliente_agregar = input("Ingrese ID Cliente agregar, ejemplo ID0000 : ")
            nombre_cliente_agregar = input("Ingrese nombre Cliente : ")
            apellido_cliente_agregar = input("Ingrese apellido Cliente agregar : ")
            edad_cliente_agregar = input("Ingrese edad Cliente agregar : ")
            contraseña_cliente_agregar = input("Ingrese contraseña Cliente agregar : " )
            agregar(clientes, id_cliente_agregar, nombre_cliente_agregar, apellido_cliente_agregar, edad_cliente_agregar, contraseña_cliente_agregar)
            print("Lista Clientes actualizada")
            print(clientes)
        elif opcion == 2:                                           # Funcion eliminar(), traspasa y recepciona parametros                                  
            eliminar(clientes)
            print("Lista Clientes actualizada")
            print(clientes)
        elif opcion == 3:                                           # Funcion mostrar(), lista los clientes
            mostrar_clientes()
        elif opcion == 4:
            break
            
            
        else:
             print("!! Opcion incorrecta")
        continuar2 = input(" Continua en Menu Principal CLIENTES s/n : ")


