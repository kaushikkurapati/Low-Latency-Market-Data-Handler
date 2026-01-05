import socket
import struct
import time
import random

group = '224.1.1.1'
port = 5004

# 2-hop restriction in network
ttl = 2
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

counter = 0
try:
    while True:
        FORMAT = '!cI4scQI'
        message_data = b'A'
        symbol_data = random.choice(["META", "AAPL", "NFLX", "GOOG", "MSFT", "TSLA"]).encode('utf-8')
        side_data = random.choice([b'B', b'S'])
        price = int(random.uniform(100, 200) * 10000)
        quantity = random.randint(1, 100)
        
        packed_struct = struct.pack(FORMAT, message_data, counter, symbol_data, side_data, price, quantity)
        
        try:
            sock.sendto(packed_struct, (group, port))
            print(f"Sent message {counter}")
        except socket.error as e:
            print(f"Socket Error {e}")
        
        counter += 1 
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\nFeed Stopped")
    sock.close()