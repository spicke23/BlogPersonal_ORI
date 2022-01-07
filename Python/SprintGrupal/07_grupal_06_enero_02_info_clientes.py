def MuestraUsuarios(info_clientes):
    print("*********************************************************************************")
    print("*********************************************************************************")
    print("Detalle de clientes")
    print("  ID usuario          Nombre              Apellido           Edad")
    for claveUsuario, detalleUsuario in info_clientes.items():
        #print("ID usuario              Nombre              Apellido           Edad")
        claveUsuario = detalleUsuario['ID_user']
        print("   ",claveUsuario,"           ",detalleUsuario['nombre'],"          ",detalleUsuario['apellido'],"          ",detalleUsuario['edad'])

def AgregaUsuario(info_clientes):
    nuevoDato = {}
    indice = len(info_clientes)+1
    ID_user = int(input("Ingrese ID de usuario: "))
    nombre = str(input("Ingrese nombre de usuario: "))
    apellido = str(input("Ingrese apellido de usuario: "))
    edad = int(input("Ingrese edad de usuario: "))
    contraseña = int(input("Ingrese contraseña de usuario: "))
    nuevoDato['ID_user'] = ID_user
    nuevoDato['nombre'] = nombre.capitalize()
    nuevoDato['apellido'] = apellido.capitalize()
    nuevoDato['edad'] = edad
    nuevoDato['contraseña'] = contraseña
    info_clientes.update({indice: nuevoDato})
    print("*********************************************************************************")
    print("***                     Usuario Ingresado con exito                           ***")
    print("*********************************************************************************")

def EliminaUsuario(info_clientes):
    nuevoDato = {}
    ID_user = int(input("Ingrese ID de usuario a eliminar: "))
    for clave, datos in info_clientes.items():
        if ID_user == datos['ID_user']:
            nuevoDato['ID_user'] = datos['ID_user']
            nuevoDato['nombre'] = datos['nombre']
            nuevoDato['apellido'] = datos['apellido']
    info_clientes.pop(clave)
    print("Usuario a eliminar:")
    print("ID:",nuevoDato['ID_user'],"nombre completo: ",nuevoDato['nombre']," ",nuevoDato['apellido'])
    print("*********************************************************************************")
    print("***                     Usuario Eliminado con exito                           ***")
    print("*********************************************************************************")

info_clientes = {
    1:{'ID_user':1456 , 'nombre': 'Maria '  , 'apellido': 'Real'    , 'edad': 25 ,'contraseña': 7852},
    2:{'ID_user':4563 , 'nombre': 'Juana  ' , 'apellido': 'Duarte'  , 'edad': 63 ,'contraseña': 5896},
    3:{'ID_user':4896 , 'nombre': 'Isabel ' , 'apellido': 'Castillo', 'edad': 32 ,'contraseña': 8563},
    4:{'ID_user':4785 , 'nombre': 'Gonzalo' , 'apellido': 'Cordoba' , 'edad': 27 ,'contraseña': 7852},
}

cierraPrograma = False
while not cierraPrograma:
    print("*********************************")
    print("¿Que operacion desea realizar?")
    print("*********************************")
    print("[ 1 ]. Mostrar Usuarios")
    print("[ 2 ]. Agregar Usuarios")
    print("[ 3 ]. Eliminar Usuarios")
    print("[ 0 ]. Finalizar Programa")
    print("*********************************")
    print("*********************************")
    opcion = int(input("Ingrese su opcion: "))

    if opcion == 1:
        MuestraUsuarios(info_clientes)
    elif opcion == 2:
        AgregaUsuario(info_clientes)
    elif opcion == 3:
        EliminaUsuario(info_clientes)
    else:
        cierraPrograma = True
