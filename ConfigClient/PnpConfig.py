import sys
import getopt
import sys
import os

pathofparent = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.append(pathofparent)
from initdb import initdbclass
from ConfigFileReader import doFileConfig
import ConfigFileReader
db=initdbclass()
#
# def usage():
#     print "--help"
#     print "--conip <ip> controldeamonIP"
#     print "--conport <port> controldeamonPort"
#     print "--contype <type> controldeamontype"
#     print "--contproto <type> controldeamonprotocol"
#     print "--inpip <ip> inputdeamonIP"
#     print "--inport <port> inputdeamonPort"
#     print "--inptype <type> inputdeamontype"
#     print "--inpproto <type> inputdeamonprotocol"
#     print "--outip <ip> outputdeamonIP"
#     print "--outport <port> outputdeamonPort"
#     print "--outtype <type> outputdeamontype"
#     print "--outproto <type> outputdeamonprotocol"
#     print "--loadfile <filename>  loadconfigdata form file"
    #ToDo add device paraemters and etc for the list
#
# try:
#     opts, args = getopt.getopt(sys.argv[1:], "h ", ["help=", "conip=","conport=","contype=","inpip=","inport=","inptype=","outip=","outport=","outtype=","loadfile=","contproto=","inpproto=","outproto="])
#     #print "Try"
# except getopt.GetoptError:
#     usage()
#
#     sys.exit(2)


def updatedata(arg,para):
    #print para
    arg=arg[2:]
    smarg=arg[1:]
    print arg,para
    #print arg
    cursor, conn = db.connecttodb()
    if(arg=="conip"):
        db.updatedatadeamondata(cursor,"ip",para,"cntrldeamon")
    elif (arg == "conport"):
        db.updatedatadeamondata(cursor, "port", para, "cntrldeamon")
    elif (arg == "contype"):
        db.updatedatadeamondata(cursor, "type", para, "cntrldeamon")
    elif (arg == "contproto"):
        db.updatedatadeamondata(cursor, "protocol", para, "cntrldeamon")
    elif (arg == "inpip"):
        db.updatedatadeamondata(cursor, "ip", para, "inpdeamon")
    elif (arg == "inpport"):
        db.updatedatadeamondata(cursor, "port", para, "inpdeamon")
    elif (arg == "inptype"):
        db.updatedatadeamondata(cursor, "type", para, "inpdeamon")
    elif (arg == "inpproto"):
        db.updatedatadeamondata(cursor, "protocol", para, "inpdeamon")
    elif (arg == "outip"):
        db.updatedatadeamondata(cursor, "ip", para, "oudeamon")
    elif (arg == "outport"):
        db.updatedatadeamondata(cursor, "port", para, "oudeamon")
    elif (arg == "outtype"):
        db.updatedatadeamondata(cursor, "type", para, "oudeamon")
    elif (arg == "outproto"):
        db.updatedatadeamondata(cursor, "protocol", para, "oudeamon")
    elif (arg == "loadfile"):
        #print "ToDo implement this part",para
        if os.path.isfile(para):
            doFileConfig(para)
        else:
            print "Sorry File not found"
    elif (smarg == "h"):
        #print usage()
        pass
    else:
        print "Wrong Argument"

    conn.commit()



