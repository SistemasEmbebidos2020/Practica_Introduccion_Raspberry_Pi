# !/usr/bin/env python3
#!/usr/bin/env python3

import subprocess
import sys
import os
import nano 

#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ubidots'])
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])
def loop():
 pass

def main():
 
 subprocess.call(['ls', '/'])
 subprocess.call(['pwd'], shell=False)
 subprocess.call(['touch', 'prueba1.py'])
 subprocess.call(['ls'], shell=False)
 while(True):
  loop()

if  __name__ ==  '__main__':
 main()
