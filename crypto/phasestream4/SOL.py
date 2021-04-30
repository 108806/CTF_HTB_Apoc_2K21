import pynput, sys, os
from pwn import xor, unhex


f = open('output.txt', 'r').read().split('\n')
enc1, enc2   = unhex(f[0]), unhex(f[1])
enc3, fpart  = xor(enc1, enc2), 'CHTB{'
exitFlag  = 0


from pynput import keyboard as kb
FPART = ''

def on_press(key):
   global FPART
   try:
      os.system('cls' if os.name == 'nt' else 'clear')
      if key == kb.Key.backspace:
         FPART = FPART[:-1]
         print('$' + FPART,xor(enc3, FPART),
            flush=False, end='\r', sep='\n')
      else:   
         FPART += key.char
         print('$ ' +FPART, xor(enc3, FPART),
               flush=False, end='\r', sep='\n')

   except AttributeError:
      print('$ ' +FPART, xor(enc3, FPART),
         flush=False, end='\r', sep='\n')

def on_release(key):
    if key == kb.Key.esc:
        # Stop listener
        return False

# Collect events until released
def collect0r():
   listener = kb.Listener(
       on_press=on_press,
       on_release=on_release)
   listener.start()

collect0r()

#GUESSING GAME BEGINS...
