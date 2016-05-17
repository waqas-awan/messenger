
import socket               # Import socket module
import sys
import select
import string

s = socket.socket()         
host = ""
port = 5104     # Reserve a port for your service.

s.connect((host, port))
while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    sys.stdout.write(data)
             
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
              
s.close()
