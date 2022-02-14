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
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #cs = client socket
        print("[C]: Client socket created")
    except socket.error as err:
        print('Client: socket open error: {} \n'.format(err))
        exit()

    port = int(sys.argv[2]) #arbritary port we can stick with for now
    localhost_addr = socket.gethostbyname(socket.gethostname()) #attaching a name to specified port (available for server (rs) too) 
    
    server_binding = (localhost_addr, port) #creative variable for connecting IP address (localhost_addr) & port
    cs.connect(server_binding) #connecting IP address & port
    
    input_file = open("PROJ2-HNS.txt")
    query_lump = input_file.read()
    queries = query_lump.splitlines()
    

    for query in queries:   
        cs.send(query.encode('utf-8'))
        time.sleep(1)

    cs.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='client', target=client)
    t1.start()
    time.sleep(1)
    print("Client: done sending queries.")