import socket
import sys
import StringIO


iplist = """198.41.0.4
192.228.79.201
192.33.4.12"""

s = StringIO.StringIO(iplist)
for line in s:
    socketload = socket.gethostbyaddr(line)
    Print socketload[0]
    with open("hostnames.txt", "a") as file:
        file.write(socketload[0]+"\n")
