import socket

def listen_on_port(port):
    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Bind the socket to a specific address and port
        sock.bind(('localhost', port))
        
        # Listen for incoming connections
        sock.listen(1)
        
        print(f"Listening on port {port}...")
        
        while True:
            # Accept a connection
            conn, addr = sock.accept()
            
            print(f"Connected by {addr}")
            
            # Receive data from the client
            data = conn.recv(1024)
            
            if not data:
                break
            
            # Process the received data
            print(f"Received data: {data.decode('utf-8')}")
            
            # Send a response back to the client
            response = "Message received"
            conn.sendall(response.encode('utf-8'))
            
    except socket.error as e:
        print(f"Socket error: {e}")
        
    finally:
        # Close the connection
        sock.close()

# Specify the port to listen on
port = 80

# Start listening on the specified port
listen_on_port(port)
