import socket
import time


def get_handshake(server_ip="127.0.0.1", server_port=8080):
	handshake_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print(f"[get_handshake] Binding to {server_ip}:{server_port}")
	handshake_socket.bind((server_ip, server_port))

	print(f"[get_handshake] Listening...")
	handshake_socket.listen(1)

	print(f"[get_handshake] Accepting...")
	client_socket, address = handshake_socket.accept()
	print(f"[get_handshake] Accepted.")

	client_ip, client_port = address
	print(f"[get_handshake] Handshake successfull! Connection from {client_ip}:{client_port}.")

	# client_socket.close()
	handshake_socket.close()

	print(f"[get_handshake] Sockets closed.")

	# return client_ip, client_port
	return client_socket


# make handshake and get ip/port
client_socket = get_handshake()
# client_socket = get_handshake('172.31.8.41',8080)

# Open the file
# with open('dsfghj.0.6.py', 'rb') as file:
with open('server_file.txt', 'rb') as file:
    # Read and send the file data in chunks
    while True:
        chunk = file.read(1024)  # Read 1024 bytes at a time
        if not chunk:
            break  # End of file
        
        # Send the chunk
        client_socket.send(chunk)

client_socket.close()
