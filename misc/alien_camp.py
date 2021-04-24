import socket, re, operator
import numpy as np

HOST,PORT = '165.227.237.7', 32355

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def netWulff(sock:socket.SOCK_STREAM):
	
	res 			= 		sock.recv(4096).decode('raw_unicode_escape')

	sock.send(b'1\n')
	help_str 		= 		sock.recv(8192)
	help_str 		+= 		sock.recv(8192)
	help_str 		= 		help_str.replace(b'\x0a', b'')[22:]
	help_str		= 		help_str.replace(b'\x09', b'')
	help_str 		= 		help_str.replace(b'r', b'')

	arr			= 		np.array(help_str)

	regex 			= 		b'[x0123456789abcdef].{3,}\s->\s\d\d\s'
	result 			= 		re.findall(regex,arr)
	nice 			= 		str(result)[2:-2]

	regex2 			= 		r'[^x][\s\d\d\s]{3,}'
	fin			= 		re.findall(regex2, nice)
	fin 			= 		iter(tuple(int(x[1:-1].strip('')) for x in fin))


	u 			= 		{
	1 : '🌞', 2 : '🍨', 3 : '❌', 4 : '🍪',
	5 : '🔥', 6 : '⛔', 7 : '🍧',  8 : '👺',
	9 : '👾', 10 : '🦄'
	}
	# 1 : b'\xf0\x9f\x8d\xa8', 2 : b'\xf0\x9f\x8c\x9e', 
	# 3 : b'\xe2\x9d\x8c', 	   4 : b'\xf0\x9f\x8d\xaa',
	# 5 : b'\xf0\x9f\x94\xa5', 6 : b'\xe2\x9b\x94', 
	# 7 : b'\xf0\x9f\x8d\xa7', 8 : b'\xf0\x9f\x91\xba',
	# 8 : b'\xf0\x9f\x91\xbe', 9 : b'\xf0\x9f\xa6\x84',
	# 10: b'\xf0\x9f\xa6\x84' 


	solvr 			= 		{x:next(fin) for x in u.values()}
	print(fin)
	print(solvr)

	ops = { "+": operator.add, "-": operator.sub,
		"*": operator.mul, "/" : operator.floordiv }


	sock.send(b'2\n')
	chall			= 		sock.recv(8192).replace(b'\x0a', b'')
	chall 			= 		chall.replace(b'\x09', b'')[101:]
	print(f'[*] GO! : {chall}')
	print(chall.decode('utf8'))


	witnessmey 		= 		0
	while b'HTB' not in chall:
		c_dead 		= 		chall.decode('utf8')

		presents 	= 		[x for x in c_dead.split() if x in solvr.keys() or x in ops]
		presents2 	= 		[solvr.get(x) or x for x in presents]
		maths 		= 		str(presents2).replace("'", "")
		maths 		= 		maths.replace(',', "")[1:-1]
		answer 		= 		str(eval(maths))
		print(answer, witnessmey)
		sock.send(bytes(answer+'\n','utf8'))
		chall 		= 		sock.recv(8192)
		witnessmey 	+= 1

	sock.close()
	return chall.decode('utf8')




r = netWulff(s)

print(r)
