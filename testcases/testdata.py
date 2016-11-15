import json
import pprint
import subprocess

import time

#subprocess.call(['python','/home/nrv/PycharmProjects/publiclink/newDeamon.py'])

# proc = subprocess.Popen(['python','/home/nrv/PycharmProjects/publiclink/newDeamon.py'])
# print proc.pid
#
# for k in range(0,150):
#     print k
#     time.sleep(1)
import pprint
import json
# fulldata={}
# data={}
# data['inpdeamon']={"ip":"127.0.0.1","port":8050,"name":'inpdeamon',"type":"server","protocol":"tcp"}
# data["oupdeamon"]={"ip":"192.168.1.6","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
# data["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
# data["next"]={"ip":"192.168.1.6","port":8888,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
#
# data["timestamp"]="2016-10-07"
# data["fromip"]="127.0.0.1"
# data["sysid"]=1500
# data["sysname"]="control1"
# data["sysname"]="control1"
# data["programproperties"]="-p 100 -q 1000"
# data["deviceproperties"]="-p 1500 -q 150"
#
# fulldata["a"]=data
#
#
# datab={}
# datab['inpdeamon']={"ip":"192.168.1.1","port":8100,"name":'inpdeamon',"type":"server","protocol":"tcp"}
# datab["oupdeamon"]={"ip":"192.168.1.3","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
# datab["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
# datab["next"]={"ip":"192.168.1.3","port":8888,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
#
# datab["timestamp"]="2016-10-07"
# datab["fromip"]="127.0.0.1"
# datab["sysid"]=1500
# datab["sysname"]="control1"
# datab["sysname"]="control1"
# datab["programproperties"]="-p 100 -q 1000"
# datab["deviceproperties"]="-p 1500 -q 150"
#
# fulldata["b"]=datab
#
#
# datac={}
# datac['inpdeamon']={"ip":"192.168.1.1","port":8100,"name":'inpdeamon',"type":"server","protocol":"tcp"}
# datac["oupdeamon"]={"ip":"192.168.1.4","port":8100,"name":'oudeamon',"type":"client","protocol":"tcp"}
# datac["cntrldeamon"]={"ip":"127.0.0.1","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
# datac["next"]={"ip":"192.168.1.4","port":8888,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
#
# datac["timestamp"]="2016-10-07"
# datac["fromip"]="127.0.0.1"
# datac["sysid"]=1500
# datac["sysname"]="control1"
# datac["sysname"]="control1"
# datac["programproperties"]="-p 100 -q 1000"
# datac["deviceproperties"]="-p 1500 -q 150"
#
# fulldata["c"]=datab
#
#
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(fulldata)
#
# print json.dumps(fulldata)

abc={"a": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.4", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "127.0.0.1", "type": "server", "port": 8050, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.4", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}, "c": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.6", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "192.168.1.1", "type": "server", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.6", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}, "b": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.6", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "192.168.1.1", "type": "server", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.6", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}}
acb={"a": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.6", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "127.0.0.1", "type": "server", "port": 8050, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.6", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}, "c": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.3", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "192.168.1.1", "type": "server", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.3", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}, "b": {"sysname": "control1", "cntrldeamon": {"ip": "127.0.0.1", "type": "client", "port": 8080, "protocol": "tcp", "name": "cntrldeamon"}, "timestamp": "2016-10-07", "fromip": "127.0.0.1", "oupdeamon": {"ip": "192.168.1.3", "type": "client", "port": 8100, "protocol": "tcp", "name": "oudeamon"}, "sysid": 1500, "inpdeamon": {"ip": "192.168.1.1", "type": "server", "port": 8100, "protocol": "tcp", "name": "inpdeamon"}, "programproperties": "-p 100 -q 1000", "next": {"ip": "192.168.1.3", "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}, "deviceproperties": "-p 1500 -q 150"}}

opt=raw_input("abc or acb ?  :- ")

import socket
import sys

fin=""
if(opt=="abc"):
    fin=abc
elif(opt=="acb"):
    fin=acb

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.3', 8888)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(json.dumps(fin))
finally:
    print >>sys.stderr, 'closing socket'
    sock.close()