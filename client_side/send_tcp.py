import sys; sys.path.append('../')
from utils_tcp import send_file


if __name__ == "__main__":
    # Usage example
    file_path = 'file.txt'
    host = '35.78.89.143'  # Server IP address
    port = 8080  # Server port number
    send_file(file_path, host, port)
