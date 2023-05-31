from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "127.0.0.1"
PORT = 5000


class postListerner(BaseHTTPRequestHandler):

    def do_POST(self):

        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        self.wfile.write(bytes('{"HELLO":"WORLD"}',"utf-8"))


server = HTTPServer((HOST,PORT), postListerner)
print("Server running...")
server.serve_forever()
server.server_close()
print("Server stopped")