import http.server
import socketserver

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Customize the response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")

def listen_on_port(port):
    # Set up the server with a custom request handler
    handler = MyRequestHandler
    server = socketserver.TCPServer(('', port), handler)

    print(f"Listening on port {port}...")

    try:
        # Start the server and keep it running until interrupted
        server.serve_forever()
    except KeyboardInterrupt:
        # Close the server gracefully on keyboard interrupt
        server.server_close()
        print("Server closed.")

# Specify the port to listen on
port = 80

# Start listening on the specified port
listen_on_port(port)
