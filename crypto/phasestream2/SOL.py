import sys
from pwn import xor, unhex
from functools import lru_cache

 
f 		= open('output.txt', 'r')
ff 		= f.read().split('\n')
ff 		= frozenset( [ x for x in ff ] )  

#flag_i = ff.index('060d11073e2b76762129761a742b1a711a2d713c363171262e38') >> 4219

# enc_flag = bytearray.fromhex('060d11073e2b76762129761a742b1a711a2d713c363171262e38')
# b_key	 = 0x45
# print(xor(enc_flag, b_key)) # b'CHTB{n33dl3_1n_4_h4yst4ck}'
# print( [ {chr(x^y):[x, y]} for x,y in zip(enc_flag, bytes([b_key]*26)) ] )


@lru_cache(maxsize=None, typed=True)
def crackr(fl:iter):

	for H in range(0xff):
		for S in fl:
			print(f'{hex(H)[2:]} : {S.strip()}' , end='\r\n', flush=False)
			bhex	= bytearray.fromhex(S)
			xord 	= xor([bhex[:5]], bytes([H]))

			if b'CHTB{' in xord: 
				return bhex, xord, H, S


print(crackr(ff))
