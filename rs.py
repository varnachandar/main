#recieves queries from client 
#forwards clients to TS1 & TS2
    #TS1 & TS2 are disjoint
#returns returned response if given w/in 5 secs (if any) to client 
    #if no response return "DomainName - TIMED OUT"
#maintains 3 connections
    #client, TS1, TS2

#must be able to accept command python rs.py rsListenPort ts1Hostname ts1ListenPort ts2Hostname ts2ListenPort
    #assigns hostname and ports where each server should listen for requests

import threading
import os
import time
import sys
import random
import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', int(sys.argv[1]))
    ss.bind(server_binding)
    ss.listen()
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    csockid, addr = ss.accept()

    data = csockid.recv(4096).decode('utf-8')

    while data:
        data = csockid.recv(4096).decode('utf-8')
        print(data)

    ss.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()
    time.sleep(1)
    print("Done.")