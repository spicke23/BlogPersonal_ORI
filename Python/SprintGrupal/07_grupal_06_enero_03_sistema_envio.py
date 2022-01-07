## Declaracion de variables y funciones
# Cada bodega será una lista
def CantidadEnvios(arreglo):
    i = len(arreglo)
    if i >= 500:
        print("Esta bodega posee más de",i," envios pendientes")

bodega_a = []
bodega_b = []

# main
cierraPrograma = False
while not cierraPrograma:
    print("Bienvenido al sistema de despacho de bodegas TeloVendo S.A.")
    print("Escoga una opcion del menu")
    print("[ 1 ] Envíos de encomiendas superiores a 1.000KM")
    print("[ 2 ] Envíos de encomiendas inferiores o igual a 1.000KM")
    print("[ 3 ] Imprimir Bodegas")
    print("[ 4 ] Finalizar")
    respuesta = int(input("Respuesta: "))
    if respuesta == 1: #Si es un envío a una distancia de más de 1.000 km es considerado largo.
        #i = len(bodega_a)
        bodega_a.append(respuesta)
        CantidadEnvios(bodega_a)
    elif respuesta == 2: #Si es un envío a una distancia igual o menor a 1.000 km es considerado rapido.
        #i = len(bodega_b)
        bodega_b.append(respuesta)
        CantidadEnvios(bodega_b)
    elif respuesta == 3: #Imprime envios de ambos tipos
        print("Cantidad de envios para Bodega_A:",len(bodega_a))
        print("Cantidad de envios para Bodega_B:",len(bodega_b))
    else:
        print("Adios")
        cierraPrograma = True


