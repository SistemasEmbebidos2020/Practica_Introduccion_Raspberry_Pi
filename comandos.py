# !/usr/bin/env python3
#!/usr/bin/env python3

import subprocess
import sys

#subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'ubidots'])
#subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade','pip'])

def main():
 
 subprocess.call(['ls', '/'])
 subprocess.call(['pwd'], shell=False) #imprimir ruta actual
 subprocess.call(['touch', 'prueba1.py']) #crear fichero
 subprocess.call(['ls'], shell=False)
 #subprocess.call(['od','-c', 'prueba1.py'], shell=False) #leer fichero
 #subprocess.call(['mkdir','holi'], shell=False)
 #subprocess.call(['python', 'prueba1.py'], shell=False) #leer fichero


if  __name__ ==  '__main__':
 main()
