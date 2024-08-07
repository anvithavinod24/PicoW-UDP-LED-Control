import socket
serverAddress = ('192.168.29.110',2222)
bufferSize = 1024
UDPClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while True:
    cmd=input("What is your command? Give Y to turn on LED and N to turn off")
    cmdEncoded=cmd.encode('utf-8')
    UDPClient.sendto(cmdEncoded,serverAddress)

