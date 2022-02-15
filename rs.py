#recieves queries from client 
#forwards clients to TS1 & TS2
    #TS1 & TS2 are disjoint
#returns returned response if given w/in 5 secs (if any) to client 
    #if no response return "DomainName - TIMED OUT"
#maintains 3 connections
    #client, TS1, TS2

#must be able to accept command "python rs.py rsListenPort ts1Hostname ts1ListenPort ts2Hostname ts2ListenPort"
    #assigns hostname and ports where each server should listen for requests

import threading
import os
import time
import sys
import random
import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for which client & rs will communicate
        print("[S]: Server socket created")
        ts1s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for which ts1 & client will communicate
        print("[S]: TS1 socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    
    #server socket connection to client
    port_client = int(sys.argv[1])
    host_client = socket.gethostname()
    print("[S]: Server host name is {}".format(host_client))
    ip_addr_client = (socket.gethostbyname(host_client))
    print("[S]: Server IP address is {}".format(ip_addr_client))


    #client socket connection to ts1
    port_ts1 = int(sys.argv[3]) #arbritary port we can stick with for now
    ip_addr_ts1 = socket.gethostbyname(sys.argv[2]) #attaching a name to specified port (available for server (rs) too) 
    #socket.gethostname() = gets current host name (E/ ilab1)
    #socket.gethostbyname(host) -> gets IP address from host name from DNS table

    server_binding_ts1 = (ip_addr_ts1, port_ts1) #making a tuple for line below, server_binding defines this particular service on our system
    ts1s.connect(server_binding_ts1)

    #server socket connection to client
    server_binding_client = (ip_addr_client, port_client) 
    ss.bind(server_binding_client)
    ss.listen(1000)


    csockid, addr = ss.accept()

    data = csockid.recv(4096).decode('utf-8')

    while data:
        data = csockid.recv(4096).decode('utf-8')
        ts1s.send(data.encode('utf-8'))
        time.sleep(1)

    time.sleep(10)
    ss.close()
    ts1s.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(1)
    print("Done.")