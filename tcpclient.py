import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Send data to the server
try:
    message = 'Hello, server!'
    client_socket.sendall(message.encode())

    # Receive response
    data = client_socket.recv(1024)
    print(f'Received: {data.decode()}')
finally:
    # Clean up the connection
    client_socket.close()
