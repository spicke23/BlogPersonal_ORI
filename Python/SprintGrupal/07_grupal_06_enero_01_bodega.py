## Librerias a utilizar
import random
import time

#productos = {}
## Definicion de variables
articulos = {
    1: {'producto': 'vasos', 'descripcion': 'producto de vidrio' },
    2: {'producto': 'cucharas', 'descripcion': 'producto con mango de madera' },
    3: {'producto': 'cuchillos', 'descripcion': 'producto con filo liso' },
    4: {'producto': 'tenedores', 'descripcion': 'producto con mango plastico' }
}

## Definicion de funciones
def CreaBodegaVirtual(**kwargs):    
    miStock = kwargs['stock']
    return miStock

def MostrarBodega(productos):
    print("******** Detalle de productos almacenados en nuestra bodega ********")
    print("ID Prod     Nombre Producto     Descripcion         Stock Disponible")
    for clave, diccionario in productos.items():
        time.sleep(1)
        print('   ',clave,'          ',diccionario['producto'],'     ',diccionario['descripcion'],'          ',diccionario['cantidad'])
    Alerta(productos)

def ActualizarBodegaVirtual(art, desc, cant, productos, operacion):
    dicNuevo = {}
    if operacion == 'ADD': ## Agrega productos nuevos a la bodega (simula promocion de productos nuevos)
        dicNuevo['producto'] = art
        dicNuevo['descripcion'] = desc
        dicNuevo['cantidad'] = cant
        indice = int(len(productos)+1)
        productos.update({indice : dicNuevo})
        return True
        #print(productos)
    elif operacion == 'DEL':  ## Elimina productos de la bodega (simula bajada de productos)
        for clave, diccionario in productos.items():
            if diccionario['producto'] == art:
                indice = clave
        productos.pop(indice)
        return True
    elif operacion == '+': ## Agrega cantidad de productos al stock (simula reposición)
        for clave, diccionario in productos.items():
            if diccionario['producto'] == art:
                indice = clave
                dicNuevo['producto'] = art
                dicNuevo['descripcion'] = diccionario['descripcion']
                dicNuevo['cantidad'] = diccionario['cantidad'] + cant
                productos.update({indice : dicNuevo})
                #print(productos)
                #break
            else:
                print("No se encuentra detalle del producto")
    elif operacion == '-': ## Quita cantidad de productos al stock (simula compra)
        for clave, diccionario in productos.items():
            if diccionario['producto'] == art:
                if cant > diccionario['cantidad']:
                    print("La cantidad a eliminar del stock es mayor a la existente")
                    break
                else:
                    indice = clave
                    dicNuevo['producto'] = art
                    dicNuevo['descripcion'] = diccionario['descripcion']
                    dicNuevo['cantidad'] = diccionario['cantidad'] - cant
                    productos.update({indice : dicNuevo})
                    #print(productos)
                    #break
            else:
                print("No se encuentra detalle del producto")
    else:
        print("Operacion no adecuada")
    Alerta(productos)

def Alerta(productos): ## Emite mensaje de alerta de productos con menos de 400 unidades
    for clave, diccionario in productos.items():
        if diccionario['cantidad'] < 400:
            cl = clave
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("El producto [",diccionario['producto'],"] posee menos de 400 unidades")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

## Programa principal
cierraPrograma = False
productos = CreaBodegaVirtual(stock=articulos)

## Pondremos la cantidad de articulos al azar en cada producto
for clave, detalle in productos.items():
    detalle['cantidad'] = random.randint(300, 500)
#print(productos)
print("***************************")
while not cierraPrograma:
    print("***************************")
    print("¿Que opcion desea realizar?")
    print("***************************")
    print("[ 1 ] Incorporar productos nuevos a la bodega")
    print("[ 2 ] Agregar productos a stock de bodega")
    print("[ 3 ] Eliminar productos de la bodega")
    print("[ 4 ] Quitar productos de stock bodega")
    print("[ 5 ] Mostrar productos de bodega")
    print("[ 0 ] Salir")

    op = int(input("*** Seleccione su opcion: "))
    operacion = ''

    if op == 1:
        print("Vamos a incorporar un articulo nuevo al stock de la bodega")
        artic = str(input("Ingrese nombre del articulo nuevo: "))
        art = artic.lower()
        descr = str(input("Ingrese descripcion del articulo nuevo: "))
        desc = descr.lower()
        cant = int(input("Ingrese cantidad del articulo nuevo: "))
        resp = ActualizarBodegaVirtual(art, desc, cant, productos, 'ADD')
        if resp == True:
            print("Articulo",art,"fue agregado con exito a nuestro stock")
        else:
            print("Ocurrio algun error y el articulo",art,"no pudo ser agregado con exito a nuestro stock")
    elif op == 2:
        print("Vamos a agregar productos al stock de bodega")
        artic = str(input("Ingrese nombre del articulo a actualizar: "))
        art = artic.lower()
        cant = int(input("Ingrese cantidad a agregar del articulo: "))
        ActualizarBodegaVirtual(art, '', cant, productos, '+')
    elif op == 3:
        print("Vamos a eliminar un articulo de la bodega")
        artic = str(input("Ingrese nombre del articulo a eliminar: "))
        art = artic.lower()
        resp = ActualizarBodegaVirtual(art, '', '', productos, 'DEL')
        if resp == True:
            print("Articulo",art,"fue eliminado con exito a nuestro stock")
        else:
            print("Ocurrio algun error y el articulo",art,"no se encuentra en nuestros registros o no pudo ser eliminado")
    elif op == 4:
        print("Vamos a quitar productos al stock de bodega")
        artic = str(input("Ingrese nombre del articulo a actualizar: "))
        art = artic.lower()
        cant = int(input("Ingrese cantidad a quitar del articulo: "))
        ActualizarBodegaVirtual(art, '', cant, productos, '-')
    elif op == 5:
        MostrarBodega(productos)
    else:
        cierraPrograma = True