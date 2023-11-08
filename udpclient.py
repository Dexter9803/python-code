import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 54321)

# Send data to the server
try:
    message = 'Hello, server!'
    client_socket.sendto(message.encode(), server_address)

    # Receive response
    data, server = client_socket.recvfrom(1024)
    print(f'Received: {data.decode()}')
finally:
    # Clean up the connection
    client_socket.close()
