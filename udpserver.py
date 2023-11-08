import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 54321)
server_socket.bind(server_address)

print('Waiting for a message...')

# Receive and send data
while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f'Received: {data.decode()}')
    server_socket.sendto(data, client_address)
