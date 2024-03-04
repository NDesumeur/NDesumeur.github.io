import http.server
import socketserver

PORT = 8000  # Vous pouvez choisir n'importe quel port disponible

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serveur démarré sur le port", PORT)
    print("Pour accéder au site, ouvrez votre navigateur et allez à l'adresse : http://localhost:{}".format(PORT))
    httpd.serve_forever()
