from random import randint 
from http.server import BaseHTTPRequestHandler, HTTPServer

def numeros_mega_sena():
    numeros = []
    for i in range(6):
        numero = randint(1,60)
        if numero not in numeros:
            numeros.append(numero)
            i = i + 1
    return numeros

print(numeros_mega_sena())

class MeuResquetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Cliente se conectou e pediu um GET")
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Servidor de numeros da mega sena")
        numeros = numeros_mega_sena()
        self.wfile.write(f'{numeros}'.encode('utf-8'))
print("-----------------------INICIANDO-SERVIDOR-----------------------")
servidor = HTTPServer( ('127.0.0.1', 80) , MeuResquetHandler)
print("-----------------------AGUARDANDO-CONEXÃO-----------------------")
servidor.serve_forever()