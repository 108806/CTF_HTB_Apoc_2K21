import base64 
print(os.getcwd())


f = open('output.txt', 'r').read()
ff = bytes(''.join([x for x in f if x not in ('\n', ' ', '\r', '\t')]), 'utf8')


def d3crypt(xstr:bytes):
	while b'CHTB' not in xstr:
		xstr = base64.b64decode(xstr)
	return xstr

print(d3crypt(ff))
