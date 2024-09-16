from http.server import BaseHTTPRequestHandler, HTTPServer
import json

lista = []
class MeuResquetHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        self.send_response(200)
        length = int(self.headers.get('content-length'))
        contato = self.rfile.read(length)
        lista.append(json.load(contato))
    def do_GET(self):
        print("Cliente se conectou e pediu um GET")
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.end_headers()
        texto_json = json.dump(lista)
        self.wfile.write(texto_json.encode('utf-8'))
        
print("-----------------------INICIANDO-SERVIDOR-----------------------")
servidor = HTTPServer( ('127.0.0.1', 80) , MeuResquetHandler)
print("-----------------------AGUARDANDO-CONEXÃO-----------------------")
servidor.serve_forever()