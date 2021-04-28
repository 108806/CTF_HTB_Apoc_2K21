from pwn import *
import os, sys
print(os.getcwd())

f = open('output.txt').read().split('\n')

enc1, enc2 = unhex(f[0]), unhex(f[1]), 
enc3 = xor(enc1, enc2)
mark = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

flag = xor(enc3, mark)
info(str(flag)[1:25])
