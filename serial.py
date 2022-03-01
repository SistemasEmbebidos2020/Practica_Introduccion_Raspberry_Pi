# !/usr/bin/env python3
# Modules
from eserial import *
from time import sleep
baudios(9600)

# Main function
def main () :

# Infinite loop
 while True :
  prints("hola como te llamas? ")
  mensaje = recibir()
  printsln("Bienvenido "+mensaje)
  pass

# Command line execution
if __name__ == '__main__' :
   main()

