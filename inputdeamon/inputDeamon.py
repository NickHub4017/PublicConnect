#ToDo add ping thread
from inputDeamonFactory import inputDeamonFactory

import time
import sys
import os
pathofparent = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(pathofparent)


from initdb import initdbclass


currentDb=initdbclass()
factory=inputDeamonFactory()
currentDb.updateinputpid(os.getgid())
def inputmainlink():
    while(1):
        isclient=True
        datarow=currentDb.getnodedata("inpdeamon")
        inpip=datarow[2]
        inpport=datarow[3]
        type="server"
        prototcol = datarow[5]
        print inpip," ",inpport," ",type
        if(type=="server" and prototcol=="tcp"):
            try:
                inputdeamon=factory.getinputDeamon("server").getconnection(inpip,inpport)
                inputdeamon.serve()
            except Exception as e:
                print e

        elif (type == "server" and prototcol == "udp"):
            try:
                inputdeamon = factory.getinputDeamon("server","udp").getconnection(inpip, inpport)
                inputdeamon.serve()
            except Exception as e:
                print e


inputmainlink()