# UDPPingerClient.py

from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12000

# Create UDP client socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout to 1 second
clientSocket.settimeout(1)

for sequence_number in range(1, 11):
    try:
        # Record send time
        send_time = time.time()

        # Create ping message
        message = f"Ping {sequence_number} {send_time}"

        # Send packet to server
        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # Receive response from server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        # Record receive time
        receive_time = time.time()

        # Calculate RTT
        rtt = receive_time - send_time

        # Print response and RTT
        print(f"Reply from {serverAddress}: {modifiedMessage.decode()}")
        print(f"RTT: {rtt:.6f} seconds")

    except timeout:
        print("Request timed out")

clientSocket.close()