
import socket
import json
import time
TCP_IP = ''
TCP_PORT = 8100
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
while(1):
    conn, addr = s.accept()
    while (1):
        x=conn.recv(1024)
        if(not x):
            break
        print str(x)
    conn.close()