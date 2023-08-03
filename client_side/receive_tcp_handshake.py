"""
Receive file through special way
"""
import socket
# from utils_tcp import receive_file
import time


# send a connection to the server
def send_handshake(server_ip="127.0.0.1", server_port=8080):
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	print(f"[send_handshake] Trying to connect to {server_ip}:{server_port}...")
	while True:
		try:
			client_socket.connect((server_ip, server_port))
			break
		except Exception as e:
			print("[send_handshake] Error:", e)
			print(f"[send_handshake] Unable to connect with {server_ip}:{server_port}. Trying Again after 3 seconds!")
			time.sleep(3)

	print(f"[send_handshake] Handshake successful!")
	# don't close the socket
	# client_socket.close()
	return client_socket

# client_socket = send_handshake()
client_socket = send_handshake('35.78.89.143',8080)

# receive_file('file.txt', "127.0.0.1", 8080)

# Open the file for writing
with open('file.txt', 'wb') as file:
    # Receive and write the file data
    while True:
        chunk = client_socket.recv(1024)  # Receive 1024 bytes at a time
        if not chunk:
            break  # End of file transmission
        
        # Write the chunk to the file
        file.write(chunk)


client_socket.close()
