import socket
import time
import argparse


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


def send_file_tcp(filename='server_test_file.txt', server_ip='172.31.36.4', server_port=8080):

    # make handshake and get ip/port
    client_socket = get_handshake(server_ip, server_port)
    
    print("[send_file_tcp] Sending file...")
    # Open the file
    with open(filename, 'rb') as file:
        # Read and send the file data in chunks
        while True:
            chunk = file.read(1024)  # Read 1024 bytes at a time
            if not chunk:
                break  # End of file
            
            # Send the chunk
            client_socket.send(chunk)
    
    print("[send_file_tcp] File sent successfully!")
    client_socket.close()
    print("[send_file_tcp] Socket Closed!")

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Send file to client')
    parser.add_argument('--filename', default='server_side/server_test_file.txt')
    parser.add_argument('--server-ip', default='172.31.36.4')
    parser.add_argument('--server-port', default=8080)
    args = parser.parse_args()
    
    send_file_tcp(filename=args.filename, server_ip=args.server_ip, server_port=args.server_port)

    
    
