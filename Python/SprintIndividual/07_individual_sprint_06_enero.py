## Librerias a utilizar
import random

## Lista con 10 futuros usuarios
# La lista contiene una lista con el nombre y apellido de futuos usuarios

futurosUsuarios = [[['Angelo'],['Valenzuela']],[['Magaly'],['Cardenas']],[['Carolina'], ['Perez']],[['Lili'], ['Soza']],[['Braulio'], ['Toro']],[['Nicolas'], ['Daneri']],[['Pablo'], ['Robles']],[['Tabatha'], ['Quiroga']],[['Susana'], ['Suares']],[['Yamna'], ['Lobos']]]
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
clave = ''
dicFuturosUsuarios = {}

## Definicion de funciones
def CreaCuentas(letraNombre,apellido):
    cuenta = str(letraNombre + apellido)
    return cuenta.lower()

def ImprimeCuenta(cuentaUsuario):
    print(cuentaUsuario)

def CreaClave(letras,numeros,clave):
    j = 0
    while j < 10:
        azar = random.randint(0,1) # azar sera letra o numero
        if azar == 1: # si es 1, azar es letra
            l = random.randint(0,1) # L sera mayuscula o minuscula
            if l == 1: # si L es 1 es mayuscula
                clave += letras[random.randint(0,25)].upper()
            else:
                clave += letras[random.randint(0,25)].lower()
        else:
            clave += numeros[random.randint(0,9)]
        j += 1
    return clave

def ValidaFono(fono):
    i = 0
    numOK = 0
    largoFono = len(fono)
    if largoFono == 8:
        while i < largoFono:
            if fono[i] in numeros:
                numOK += 1
                i += 1
                if numOK == largoFono:
                    return str(fono)
            else:
                print("El numero ingresado contiene otros caracteres")
                fono = str(input("Vuelva a ingresar el fono: "))
                ValidaFono(fono)
    else:
        if largoFono < 8 or largoFono > 8:
            print("La cantidad de digitos del fono no coincide")
            fono = str(input("Vuelva a ingresar el fono: "))
            ValidaFono(fono)

def CreaListadoNuevosUsuarios(dicFuturosUsuarios,nombre,apellido,cuenta,password,fono):
    dicNuevoUsuario = {}
    largo = len(dicFuturosUsuarios) + 1
    dicNuevoUsuario['nombre'] = nombre
    dicNuevoUsuario['apellido'] = apellido
    dicNuevoUsuario['cuenta'] = cuenta
    dicNuevoUsuario['password'] = password
    dicNuevoUsuario['fono'] = fono
    dicFuturosUsuarios.update({largo : dicNuevoUsuario})

## Principal
i = 0
## Ciclo que llama a las funciones para cargar y validar campos del diccionario que contendra la
## info final de los futuros usuarios
for usuarios in futurosUsuarios:
    nombre = usuarios[0][0]
    apellido = usuarios[1][0]
    letra = nombre[0]
    cuenta = CreaCuentas(letra, apellido)
    password = CreaClave(letras,numeros, clave)
    telefono = str(input(f"Ingrese numero de telefono para usuario " + nombre + " " + apellido + ": "))
    fono = ValidaFono(telefono)
    CreaListadoNuevosUsuarios(dicFuturosUsuarios,nombre,apellido,cuenta,password,fono)
    #AgregaFonoNuevosUsuariosfonouarios,fono)
#print(dicFuturosUsuarios)
