import socket
import struct

MCAST_GRP = '224.1.1.1'
MCAST_PORT = 5004

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
except AttributeError:
    pass

sock.bind(('', MCAST_PORT))
mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

FORMAT = '!cI4scQI'
print(f"Listening on udp://{MCAST_GRP}:{MCAST_PORT}")

while True:
    data, address = sock.recvfrom(1024)
    if data:
        try:
            unpacked_data = struct.unpack(FORMAT, data)
            message_type = unpacked_data[0].decode('ascii')
            counter_val = unpacked_data[1]
            symbol = unpacked_data[2].decode('utf-8').strip('\0')
            side = unpacked_data[3].decode('ascii')
            price = unpacked_data[4]
            quantity = unpacked_data[5]
              
            print(f"Received from {address}: Message='{message_type}', Counter={counter_val}, Symbol={symbol}, Side={side}, Price={price}, Quantity={quantity}")
            
        except struct.error as e:
            print(f"Error unpacking data: {e}")
