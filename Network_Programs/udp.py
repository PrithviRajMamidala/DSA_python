import argparse, socket

MAX_SIZE_BYTES = 65535

def server(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
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

def client(port):
    host = '127.0.0.1'
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((host, port))
    message = input('Input lowercase sentence:')
    data = message.encode('ascii')
    s.send(data)
    print('The OS assigned the address {} to me'.format(s.getsockname()))
    data = s.recv(MAX_SIZE_BYTES)
    text = data.decode('ascii')
    print('The server replied with {!r}'.format(text))

if __name__ == '__main__':
    funcs = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='UDP client and server')
    parser.add_argument('functions', choices=funcs, help='clent or server')
    parser.add_argument('-p', metavar='PORT', type=int, default=3000, help='UDP port (default 3000)')
    args =parser.parse_args()
    function = funcs[args.functions]
    function(args.p)