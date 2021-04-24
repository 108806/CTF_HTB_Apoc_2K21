import socket


HOST, PORT = '0.0.0.0', 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
print(s)

while True:
    s.listen()
    slave, addr = s.accept()
    print(f'[*] {slave} : {addr}')
    data = slave.recv(8192)
    print('[*]', data.decode(), '[*]')

    sfile = slave.makefile('rwb', 0)
    line = data.split(b'\n')[0]
    
    content = b''
    content += f'<html><head><title>Welcome {addr} </title></head>'.encode('iso-8859-1')
    content += b'<body><h1>Follow the link...</h1>'
    content += b'All the server needs to do is '
    content += b'to deliver the text to the socket. '
    content += b'It delivers the HTML code for a link, '
    content += b'and the web browser converts it. <br><br><br><br>'
    # content += b'<font size="7"><center> <a href="http://python.about.com/index.html">Click me!</a> </center></font>'
    content += f'<br><br>The wording of your request was: "{line}"'.encode('iso-8859-1')
    content += b'</body></html>'

    sfile.write(b'HTTP/1.0 200 OK\n')
    sfile.write(f'Content-Length: {len(content)}\n\n'.encode('iso-8859-1'))
    sfile.write(content)
    sfile.close()
