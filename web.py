from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        self.wfile.write(self.get_response().encode("utf-8"))

    #Home Page
    def get_response(self):
        #Error si la url es distinta a "/"
        if self.path != "/":
            return """<h1>Error 404</h1>"""
        #Si la url esta en home despliega la página
        return """<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Ana Lee </title>
    <link href="css/style.css" rel="stylesheet">
  </head>
  <body>
 <h1>Ana Lee </h1> 
    <h2>Desarrolladora Web (Música/Diseño/Empresaria)</h2>
    <small>Este texto fue generado por Copilot:</small>
    <h3>
      ¡Hola! Soy Ana Lee, una desarrolladora web que se especializa en la
      creación de sitios web y aplicaciones web. Me encanta trabajar con
      tecnologías web modernas y crear experiencias de usuario atractivas y
      fáciles de usar. También soy una artista y empresaria apasionada, y me
      encanta combinar mi creatividad y mi pasión por la tecnología para crear
      soluciones web únicas y efectivas. .
    </h3>
    </br>
    <h2>Proyectos</h2>
    <h3><a href="/proyecto/1"> Web Estática  - App de recomendación de libros </a></h3>
    <h3><a href="/proyecto/2"> Web App - MeFalta, que película o serie me falta ver </a></h3>
    <h3><a href="/proyecto/3"> Web App - Foto22,  web para gestión de fotos </a></h3>
    </br>
    <h2>Experiencia</h2>
    <h3>Desarrolladora Web Freelance</h3>
    <h3>Backend: FastAPI, nodejs, Go</h3>
    <h3>Frontend: JavaScript, htmx, React</h3>
  </body>
</html>
"""
        

if __name__ == "__main__":
    print("Starting server")
    #Cambio de puerto de "8080" a "8000"
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
