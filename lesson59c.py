import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as c:
    c.bind("127.0.0.1", 50008)