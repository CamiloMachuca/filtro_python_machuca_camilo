import json
def mostrarservicios():
    with open('servicios.json','r') as openfile:
        listaServicios=("servicios.json", openfile)
    return listaServicios
    
def guardarServicios(miDato):
    with open('servicios.json','w') as openfile:
        listaServicios=("servicios.json",miDato, openfile)
    return listaServicios


import json
def mostrarUsuarios():
    with open('usuarios.json','r')as openfile:
        listaUsuarios=('usuarios.json', openfile)
    return listaUsuarios

def guardarUsuarios(miDato):
    with open('usuarios.json','w')as openfile:
        listaUsuarios=('usuarios.json', miDato, openfile)
    return listaUsuarios
    


print("############################")
print("=========Bienvenido=========")
print("############################")
print()
buclePrincipal=True
while buclePrincipal==True:
    print("//////////////////////////////////////")
    print("=============MENU PRINCIPAL===========")
    print("//////////////////////////////////////")
    print("(1) usuarios")
    print("(2) Administrador")
    print("(3) salir del programa")
    opcion=input("Ingrese la opcion deseada: ")
    if opcion=="1":
        bucleUsuarios=True
        while bucleUsuarios==True:

            print("#####################################")
            print("============MENU USUARIOS============")
            print("#####################################")
            print("(1) ver servicios disponibles")
            print("(2) Realizar consulta")
            print("(3) volver al menu principal")
            opc=input("Ingrese la opcion deseada: ")
            print()


            if opc=="1":
                print("Los servicios disponibles son: ")
                listaservi=[]
                listaservi=mostrarservicios()
                for i in listaservi:
                    print(["id"],i["id"])
                    print(["tipo"],i["tipo"])
                    print(["caracteristicas"],i["caracteristicas"])
            elif opc=="2":
                listausuario=[]
                listausuario=mostrarUsuarios()
                print("Que tipo de consulta quieres realizar (reclamaciones, sugerencias): ")
                consulta=input("Ingrese la consulta a realizar: ")
                ingresa_id=input("Ingrese tu id para verificar tus datos")
                for i in listausuario:
                    for usuario in id["id"]:
                        if usuario["id"]==ingresa_id:
                            print("usuario verificado correctamente")
                            usuario["seguimiento_usuario"]= consulta
                            listausuario.append["seguimiento_usuario"]
                            guardarUsuarios(listausuario)
                        else:
                            print("usuario no encontrado en la base de datos")
            elif opc=="3":
                print("se regreso al menu principal")
                bucleUsuarios=False
            else:
                print("Porfavor ingrese una opcion valida")

      

    elif opcion=="2":
        bucleAdministrador=True
        while bucleAdministrador==True:
            print("#####################################")
            print("============MENU ADMINISTRADOR=======")
            print("#####################################")
            print("(1) ver registros de usuarios")
            print("(2) Agregar un nuevo cliente")
            print("(3) eliminar un cliente")
            print("(4) modulo de gestion de servicios")
            print("(5) modulo de Reportes")
            print("(6) modulo de bonificacion para clientes leales")
            print("(7) volver al menu principal")
            respuesta=input("Ingrese la opcion deseada: ")
            print()
            if respuesta=="1":
                usuarios=mostrarUsuarios
                print("Los usuarios registrados son:")
                for i in usuarios:
                    print(["id"],i["id"])
                    print(["nombre"],i["nombre"] )
                    print(["apellidos"],i["apellidos"])
                    print(["direccion"],i["direccion"])
                    print(["informacionDeContacto"],i["informacionDeContacto"])
                    print(["TipoCliente"],i["TipoCliente"])
                    print(["serviciosUtilizados"],i["serviciosUtilizados"])
                    print(["seguimiento_usuario"],i["seguimiento_usuario"])
                    print(["permanencia"],i["permanencia"])
                    print()
            elif respuesta=="2":
                print("Ingrese los datos del nuevo cliente")
                nuevoCliente={}
                nuevoCliente["id": int(input("Ingrese el id que va a tener el usuario"))]
                nuevoCliente["nombre": input("Ingrese el nombre del usuario: ")]
                nuevoCliente["apellidos": input("Ingrese los apellidos del nuevo cliente: ")]
                nuevoCliente["direccion": input("Ingrese la direccion del nuevo cliente: ")]
                nuevoCliente["informacionDeContacto": input("Ingrese el numero telefonico: ")]
                nuevoCliente["TipoCliente": input("Ingrese el tipo de cliente que es (nuevo, regular o leales): ")]
                nuevoCliente["serviciosUtilizados": input("Ingrese el servicio que utiliza el cliente: ")]
                nuevoCliente["seguimiento_usuario": input("ingrese si el cliente tiene (reclamaciones, sugerencias): ")]
                nuevoCliente["permanencia": input("Ingrese la permanencia del cliente: ")]

                guardarUsuarios(nuevoCliente)

            elif respuesta=="3":
                print()
                clientes=mostrarUsuarios
                print("Ingrese el id del cliente que deseas eliminar")
                eliminar_id=int(input())
                for cliente in clientes:
                    for usuarios in cliente["id"]:
                        if cliente["id"]==eliminar_id:
                            print()
            elif respuesta=="4":
                bucleServicios=True
                while bucleServicios==True:
                    print("###########################################")
                    print("========= MENU GESTION DE SERVICIOS=======")
                    print("###########################################")
                    print("(1) Agregar un nuevo servicio")
                    print("(2) modificar un servicio")
                    print("(3) eliminar un servicio")
                    print("(4) regresar al menu anterior")
                    opci=input("Ingresa la opcion deseada: ")
                    print()
                    if opci=="1":
                        print("Ingrese los datos del nuevo servicio")
                        nuevoServicio={}
                        nuevoServicio["id": int(input("Ingrese el id del nuevo servicio: "))]
                        nuevoServicio["tipo": input("Ingrese el tipo de servicio que va a hacer: ")]
                        nuevoServicio["caracteristicas": input("Ingrese las caracteristicas del nuevo servicio: ")]
                        nuevoServicio["precio": input("ingrese el coste del nuevo servicio: ")]
                        guardarServicios(nuevoServicio)
                        print()
                    elif opci=="2":
                        listaser=mostrarservicios
                        servicio_id=int(input("ingrese el id del evento a eliminar: "))
                        for servicio in listaser:
                            for servi in servicio["id"]:
                                if servicio["id"]==servicio_id:
                                    print()#falta eliminar servicio
                    elif opci=="3":
                        print("se regreso al menu anterior")
                        bucleServicios=False
                        

            elif respuesta=="5":
                print("##############################")
                print("=========MENU REPORTES========")
                print("##############################")
                print("(1) ver cantidad de productos/servicios ofrecidos por la empresa")
                print("(2) ver productos mas populares que se presentan en la enpresa")
                print("(3) ver usuarios que han adquirido cada servicio y con ello la cantidad de este mismo ")
                respuest= input("Ingrese la opcion deseada: ")
                print()
                if respuest=="1":
                    
                    cantidad=[]
                    print("Los cantidad de productos/servicios ofrecidos por la empresason son: ")
                    listaservi=mostrarservicios()
                    for i in listaservi:
                        print(["id"],i["id"])
                        print(["tipo"],i["tipo"])
                        print(["caracteristicas"],i["caracteristicas"])

            elif respuesta=="6":
                print("modulo de bonificacion para clientes leales")
                clientesBonificados=[]
                clientes=mostrarUsuarios
                for client in clientes:
                    for cliente in client["permanencia"]:
                        if client["permanencia"]>10:
                            clientesBonificados= client
            elif respuesta=="7":
                print("se volvio al menu principal")
                bucleAdministrador=False


    elif opcion=="3":
        print("Gracias por participar asta luego")
        buclePrincipal=False

    else:
        print("porfavor ingrese una opcion valida")

#programa desarrollado por Camilo Machuca vega