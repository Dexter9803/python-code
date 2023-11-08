import socket

def send_message(sock, message):
    sock.send(message.encode())

def receive_message(sock):
    data = sock.recv(1024)
    return data.decode()

def main():
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the server's hostname and port
    host = "Prashant"  # Replace with the actual hostname or IP address of the server
    port = 12345
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Receive a message from the server
    received_message = receive_message(client_socket)
    print(f"Received message from server: {received_message}")
    
    # Send a message to the server
    send_message(client_socket, "Hello from client!")
    
    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
