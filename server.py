import socket

def send_message(sock, message):
    sock.send(message.encode())

def receive_message(sock):
    data = sock.recv(1024)
    return data.decode()

def main():
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name and port
    host = socket.gethostname()
    port = 12345
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    
    print(f"Waiting for connection on {host}:{port}...")
    
    # Accept the connection
    client_socket, addr = server_socket.accept()
    
    print(f"Connection established with {addr}")
    
    # Send a message to the client
    send_message(client_socket, "Hello from server!")
    
    # Receive a message from the client
    received_message = receive_message(client_socket)
    print(f"Received message from client: {received_message}")
    
    # Close the sockets
    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
