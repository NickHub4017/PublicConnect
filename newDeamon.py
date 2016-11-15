import json
import os
import socket
import sys

from initdb import initdbclass


def writeToPipe(msg):
    path = "/tmp/control"
    try:
        os.mkfifo(path)
    except Exception as e:
        pass
    fifo = open(path, "w")
    fifo.write(msg)
    fifo.close()

HOST = ''	# Symbolic name, meaning all available interfaces
PORT = 8888	# Arbitrary non-privileged port

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
    sock.bind((HOST, PORT))
except socket.error as msg:
	print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
	sys.exit()

print 'Socket bind complete'

#Start listening on socket
sock.listen(10)
print 'Socket now listening'
db=initdbclass()
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = sock.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    findata=""
    #conn.send(db.getnodedata("processname"))  # Sending ID
    while True:
        data = conn.recv(1024)
        if(not data):
            break
        findata=findata+data
        if not data:
            break
    writeToPipe(findata)
    conn.close()
    cur=json.loads(findata)
    HOSTNEXT = cur[db.getdata("processname")]["next"]["ip"]  # The remote host
    if(not "0.0.0.0" in HOSTNEXT):
        PORTNEXT = 8888  # The same port as used by the server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((HOSTNEXT, PORTNEXT))
            s.sendall(findata)
            s.close()
        except:
            pass
    else:
        print "I am the End"
sock.close()