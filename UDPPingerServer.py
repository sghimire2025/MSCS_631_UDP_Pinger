# UDPPingerServer.py

import random
from socket import *

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(("", 12000))

print("UDP Ping Server is running on port 12000...")
print("Waiting for client messages...\n")

while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)

    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)

    decoded_message = message.decode()
    print(f"Received from {address}: {decoded_message}")

    # Capitalize the message from the client
    response_message = message.upper()

    # If rand is less than 4, consider the packet lost and do not respond
    if rand < 4:
        print(f"Simulating packet loss for message from {address}\n")
        continue

    # Otherwise, the server responds
    serverSocket.sendto(response_message, address)
    print(f"Sent to {address}: {response_message.decode()}\n")