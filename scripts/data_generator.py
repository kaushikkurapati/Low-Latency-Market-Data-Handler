import socket

localIP = "0.0.0.0"
localPort = 20001
bufferSize = 1024

msgFromServer = "Hello World\n"

bytesToSend = str.encode(msgFromServer)
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("UDP Server Up and Listening")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    
    clientMsg = "Message from client: {}".format(message.decode())
    clientIP = "Client IP Address: {}".format(address)
    
    print(clientMsg)
    print(clientIP)

