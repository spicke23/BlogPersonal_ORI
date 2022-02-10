from http.server import HTTPServer, BaseHTTPRequestHandler
from logging import Handler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('Hola Ta!'.encode())

def main():
    PORT = 8000
    server = HTTPServer(('',PORT), Handler)
    print('Servidor corriendo en puerto %s' % PORT)
    server.serve_forever()

if __name__=='__main__':
    main()


#-----------------PREGUNTAS TEORICAS-------------

#Identifique qué paquetes se descargan automáticamente y su utilidad

# Django-watson (Búsquedas)
# DRF (REST)
# Graphene (Graphql)
# Django-rest-auth (Autenticación)
# Django-allauth (Autenticación)
# Django-filter (Búsquedas)
# Django-storage (AWS storage)
# Django-braces (Funciones comunes)

#Ventajas de usar Django?

# Me permite tener una idea a un prototipo funcional rápido 
#Cualquier cosa que se necesite realizar, ya estará implementada, sólo hay que adaptarla a nuestras necesidades. 


#¿Qué desventajas nos trae este tipo de proyectos sin Django?

# Para algunos de los módulos funcionales que no se requieren para algunas aplicaciones livianas, también se incluye Django, no es tan ligero para el matraz.

#Se han encapsulado muchas clases y métodos, y se utilizan directamente, pero es más difícil cambiarlo.

#El rendimiento de Django es bajo en comparación con C, el rendimiento de C ++, por supuesto, esta es la olla de Python, y otros marco de Python tendrán el mismo problema después del tráfico.

#La plantilla de Django implementa el código y el estilo completamente separados, y no permite el código de Python en la plantilla, la flexibilidad puede no ser suficiente.



