import sys; sys.path.append('../')
from utils_tcp import receive_file


if __name__=="__main__":
    # Usage example
    file_path = 'file.txt'
    host = '127.0.0.1'  # Server IP address
    port = 12345  # Server port number
    receive_file(file_path, host, port)
