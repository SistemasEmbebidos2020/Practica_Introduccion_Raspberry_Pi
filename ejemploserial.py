# !/usr/bin/env python3
# Modules

from eserial import *
from time import sleep

baudios(9600)
sleep(0.3)
nomina = ["tonny","alisson","christopher","victor"]
clave = ["1234","2345","3456","4567"]

def verificacion(Name):
 for i in range(len(nomina)):
  if Name == nomina[i]:
   printsln ("Hello "+ nomina[i])
   sleep(0.2)
   prints ("Whats your password? ")
   passw = recibir ()
   sleep(0.2)
   if passw == clave[i]:
    printsln ("Welcome to ESPOL ")
   else:
    printsln ("passw incorrecta ")
   return
   sleep(0.2)

# Main function
def main () :

# Infinite loop
 while True :
  prints("hola como te llamas? ")
  mensaje = recibir()
  verificacion(mensaje)
  pass

# Command line execution
if __name__ == '__main__' :
   main()
 
