import socket

MAX_SIZE_BYTES = 65535 # Size of UDP datagram in Bytes

# setting up a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = 3000
hostname = '127.0.0.1'
s.bind((hostname, port))
print('Listening at {}'.format(s.getsockname()))

while True:
    data, clientAddr = s.recvfrom(MAX_SIZE_BYTES)
    message = data.decode('ascii')
    upperCaseMessages = message.upper()
    print('The client at {} says {!r}'.format(clientAddr, message))
    data = upperCaseMessages.encode('ascii')
    s.sendto(data, clientAddr)
    