from pwn import * 

lines = read('output.txt').splitlines()

def crckr():
	for i in range(0xff):
		info('XORin\' lines with %#x', i)
		byte = bytes([i])
		for l in lines:
			xored = xor(unhex(l), byte)
			if b'CHTB{' in xored:
				return(xored, l, byte)

print(crckr())
