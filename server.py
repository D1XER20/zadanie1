import http.server
import socketserver
import datetime

# Ustawienia serwera
PORT = 8000
author_name = "Ivan Zachatka"

# Logowanie informacji o uruchomieniu serwera
print("Server started at", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print("Author:", author_name)
print("Listening on port", PORT)

# Klasa serwera, dziedzicząca po klasie SimpleHTTPRequestHandler
class MyServer(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Wyświetlenie strony z informacjami o kliencie
        client_ip = self.client_address[0]
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><body>", "utf-8"))
        self.wfile.write(bytes("Your IP address is: " + client_ip + "<br>", "utf-8"))
        self.wfile.write(bytes("Current time in your timezone is: " + str(datetime.datetime.now()) + "<br>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

# Uruchomienie serwera na podanym porcie
with socketserver.TCPServer(("", PORT), MyServer) as httpd:
    httpd.serve_forever()
