
from inputDeamonServer import inputDeamonServer
from inputDeamonUDPServer import inputDeamonUDPServer

class inputDeamonFactory:
    def __init__(self):
        print "init factory"

    def getinputDeamon(self,type,protocol="tcp"):
        if(type=="server" and protocol=="tcp"):
            return inputDeamonServer()
        elif (type == "server" and protocol == "udp"):
            return inputDeamonUDPServer()
