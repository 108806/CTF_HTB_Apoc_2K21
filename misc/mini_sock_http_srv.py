import socket

HOST, PORT = '', 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen()
print(s)
index = open('index.html', 'rb')

while True:
    slave, addr = s.accept()
    slave.send(b'HTTP/1.0 200 OK\r\n\r\n')
    slave.sendfile(index, 0)
    print(f'[*] {slave} : {addr}')
    data = slave.recv(8192)
    print('[*]', data.decode(), '[*]')

