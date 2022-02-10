from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        self.wfile.write('Servidor levantado mediante http.server'.encode())

def main():
    PORT = 8000
    server = HTTPServer(('', PORT), Handler)
    print('El servidor se encuentra corriendo en puerto %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()