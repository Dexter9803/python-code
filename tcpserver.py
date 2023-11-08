import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Waiting for a connection...')

# Accept a connection
client_socket, client_address = server_socket.accept()
print(f'Connection established with {client_address}')

# Receive and send data
try:
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f'Received: {data.decode()}')
        client_socket.sendall(data)
finally:
    # Clean up the connection
    client_socket.close()
    server_socket.close()
