# bflag = bytearray.fromhex('2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904')
# bk 		= tuple(x ^ y for x, y in zip(bflag[:5], b'CHTB{'))

# result = []
# for i in range(0, len(bflag), 5):
# 	result += ''.join( [chr(x ^ y) for x, y in zip(bflag[i:i+5], bk)] )

# print(''.join(result))

# Same as :

from pwn import xor, unhex

bflag, beg = unhex('2e313f2702184c5a0b1e321205550e03261b094d5c171f56011904'), 'CHTB{'
bk = xor(bflag[:5], beg)
print(xor(bflag,bk))
