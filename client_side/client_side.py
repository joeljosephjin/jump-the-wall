"""
Receive file through special way
"""
import socket
import time
import argparse


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

def receive_file_tcp(filename='client_test_file.txt', ip='35.78.89.143', port=8080):
    # client_socket = send_handshake()
    client_socket = send_handshake(ip, port)

    # Open the file for writing
    with open(filename, 'wb') as file:
        # Receive and write the file data
        while True:
            chunk = client_socket.recv(1024)  # Receive 1024 bytes at a time
            if not chunk:
                break  # End of file transmission
            
            # Write the chunk to the file
            file.write(chunk)


    client_socket.close()

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Receive file from client')
    parser.add_argument('--server-ip', default='54.95.32.16')
    parser.add_argument('--server-port', default=8080)
    args = parser.parser_args()
    receive_file_tcp(filename='client_test_file.txt', ip=args.server_ip, port=args.server_port)


