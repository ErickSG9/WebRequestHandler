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

    #HTML dinámico
    def get_response(self):
        #Formato para los elementos path 
        P = self.url().path.split("/")[1:]
        path = ": ".join(P)

        #Extraer los datos del url
        D = parse_qsl(self.url().query)
        Q = [x for x in D]
        query = ""
        if Q:
            #Formato para los elementos query
            q = [f"{y}: {z}" for (y, z) in Q]
            query = ", ".join(q)

        #Regresar los datos ordenados del path y query
        return f"""         <h1> {path} {query} </h1>           
"""
        #Al introducir el comando "curl http://localhost:8000/Proyecto/web-uno?Autor=luis"
        #regresara "<h1> Proyecto: web-uno Autor: luis </h1>"

if __name__ == "__main__":
    print("Starting server")
    #Cambio de puerto de "8080" a "8000"
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
