#sends queries to RS from input file PROJ2-HNS.txt
#directly prints output received from RS into output file, RESOLVED.txt

#should accept command "python client.py rsHostname rsListenPort"
    #allocates RS host name and listening port 

import threading
import os
import time
import sys
import random
import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket for which client & rs will communicate
        print("[C]: Client socket created")
    except socket.error as err:
        print('Client: socket open error: {} \n'.format(err))
        exit()

    port = int(sys.argv[2]) #arbritary port we can stick with for now
    ip_addr = socket.gethostbyname(sys.argv[1]) #attaching a name to specified port (available for server (rs) too) 
    #socket.gethostname() = gets current host name (E/ ilab1)
    #socket.gethostbyname(host) -> gets IP address from host name from DNS table

    server_binding = (ip_addr, port) #making a tuple for line below, server_binding defines this particular service on our system
    cs.connect(server_binding) #connecting socket to IP address & port
    
    input_file = open("PROJ2-HNS.txt")
    query_lump = input_file.read()
    queries = query_lump.splitlines()
    

    for query in queries:   
        cs.send(query.encode('utf-8'))
        time.sleep(1) #to ensure packets are sent separately and not conjoint

    cs.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='client', target=client)
    t1.start()
    time.sleep(1)
    print("Client: done sending queries.")