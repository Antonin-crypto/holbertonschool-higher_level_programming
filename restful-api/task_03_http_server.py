#!/usr/bin/python3
"""contains Develop a simple API using Python with the `http.server` module"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHandler(BaseHTTPRequestHandler):
    """contais the class"""
    def do_GET(self):
        # Gérer les requêtes GET
        if self.path == '/':
            # Endpoint racine: retourner un message texte simple
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # Endpoint /data: retourner des données JSON
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            json_data = json.dumps(data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_data.encode('utf-8'))
        elif self.path == '/status':
            # Endpoint /status: retourner le statut de l'API
            status_data = {
                "status": "OK"
            }
            json_status = json.dumps(status_data)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json_status.encode('utf-8'))
        else:
            # Gérer les endpoints non définis avec une réponse 404
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    """run of server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting HTTP server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
