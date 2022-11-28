from pyautogui import press, typewrite, hotkey
import time

from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "192.168.1.24"
serverPort = 80

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if (self.path == "/up"):
            press('up')

        if (self.path == "/down"):
            press('down')

        if (self.path == "/left"):
            press('left')

        if (self.path == "/right"):
            press('right')

        print(self.requestline)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Apple Watch Remote Control by Sebastien Bonnet</title></head>", "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


webServer = HTTPServer((hostName, serverPort), MyServer)
print("Server started http://%s:%s" % (hostName, serverPort))

try:
    webServer.serve_forever()
except KeyboardInterrupt:
    pass

webServer.server_close()
print("Server stopped.")
