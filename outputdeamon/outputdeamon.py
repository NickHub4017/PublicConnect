#ToDo add ping thread
from outputDeamonFactory import outputDeamonFactory

import time
import sys
import os
pathofparent = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(pathofparent)


from initdb import initdbclass


currentDb=initdbclass()
factory=outputDeamonFactory()  #ToDo
currentDb.updateoutputpid(os.getgid())
def outputmainlink():#ToDo
    while(1):
        isclient=True
        datarow=currentDb.getnodedata("oudeamon")#ToDo
        outpip=datarow[2]#ToDo
        outpport=datarow[3]#ToDo
        type="client"
        protocol = datarow[5]
        print protocol,"-----"
        #time.sleep(10)
        print outpip," ",outpport," ",type," ",os.getpid()#ToDo
        if(type=="client" and protocol=="tcp"):
            outputdeamon = factory.getoutputDeamon("client").getconnection(outpip,outpport)#ToDo

            while(not outputdeamon.connect()):#ToDo
                time.sleep(2)
                print "output Link Connection error occured"
            try:
                outputdeamon.senddata()#ToDo
                print "outclient"
            except Exception,e:
                print "output Server Link gone ",e
                outputdeamon.disconnect()#ToDo
        elif(type == "client" and protocol == "udp"):
            outputdeamon = factory.getoutputDeamon("client","udp").getconnection(outpip, outpport)  # ToDo

            while (not outputdeamon.connect()):  # ToDo
                time.sleep(2)
                print "output Link Connection error occured UDP"
            try:
                outputdeamon.senddata()  # ToDo
                print "outclient"
            except Exception, e:
                print "output Server Link gone ", e
                outputdeamon.disconnect()  # ToDo


outputmainlink()