import socket
import time


def send_file(file_path, host, port):
    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print("[send_file] Connecting to Server...")
    # Connect to the server
    while True:
        try:
            client_socket.connect((host, port))
            print("[send_file] Connected to Server.")
            break
        except Exception as e:
            print(f"[send_file] Error: {e}!")
            print(f"[send_file] Trying again in 3 seconds.")
            time.sleep(3)
    
    # Open the file
    with open(file_path, 'rb') as file:
        # Read and send the file data in chunks
        while True:
            chunk = file.read(1024)  # Read 1024 bytes at a time
            if not chunk:
                break  # End of file
            
            # Send the chunk
            client_socket.send(chunk)
    
    print("[send_file] File Sent.")
    # Close the socket
    client_socket.close()
    print("[send_file] Socket closed.")


def receive_file(file_path, host, port):
    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    print(f"[receive_file] Binding to port {port}...")
    # Bind the socket to a specific IP address and port
    while True:
        try:
            server_socket.bind((host, port))
            print(f"[receive_file] Binded to port {port}")
            break
        except Exception as e:
            print(f"[receive_file] Error: {e}!")
            print(f"[receive_file] Trying again in 3 seconds!")
            time.sleep(3)
    
    print(f"[receive_file] Listening to port {port}")
    # Listen for incoming connections
    server_socket.listen(1)
    
    # Accept a client connection
    print(f"[receive_file] Accepting connections")
    client_socket, address = server_socket.accept()
    print(f"[receive_file] Accepted connection")
    
    # Open the file for writing
    with open(file_path, 'wb') as file:
        # Receive and write the file data
        while True:
            chunk = client_socket.recv(1024)  # Receive 1024 bytes at a time
            if not chunk:
                break  # End of file transmission
            
            # Write the chunk to the file
            file.write(chunk)
    
    print(f"[receive_file] File sent successfully!")
    # Close the connection and the socket
    client_socket.close()
    server_socket.close()
    print(f"[receive_file] Sockets closed.")
