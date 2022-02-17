#will read DNS table from input file PROJ2-DNTS2.txt
#returns "DomainName IPaddress A IN" if domain name is found (case insensitive)
#returns null otherwise

#must be able to accept command "python ts2.py ts2ListenPort" and listen on that port
        #assigns port for ts1 to listen for requests at

import threading
import os
import time
import json 
import sys
import random
import socket

def server2():
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for which client & rs will communicate
        print("[TS2]:  socket created")
    except socket.error as err:
        print('[TS2]: socket open error: {} \n'.format(err))
        exit()


    port = int(sys.argv[1])
    host = socket.gethostname()
    print("[TS2]: host name is {}".format(host))
    ip_addr = (socket.gethostbyname(host))
    print("[TS2]: Server IP address is {}".format(ip_addr))

    server_binding = (ip_addr, port) 
    ts2.bind(server_binding)
    ts2.listen(1000)
    csockid, addr = ts2.accept()

    dns_table = open("PROJ2-DNSTS2.txt")
    dictionary = {}

    for entry in dns_table:
        key, value, A = entry.split()
        key.lower()
        dictionary[key] = value

    print(dictionary)
        

    data = csockid.recv(4096).decode('utf-8')

    while data:
        print(data)
        data.lower()

        if data in dictionary:
            domainName = json.dumps((data, dictionary.get(data)))
        else:
            domainName = "null"

        csockid.send(domainName.encode('utf-8'))
        data = csockid.recv(4096).decode('utf-8')

    ts2.close()
    exit()


if __name__ == "__main__":
    t1 = threading.Thread(name='server2', target=server2)
    t1.start()
    time.sleep(1)
    print("Done.")