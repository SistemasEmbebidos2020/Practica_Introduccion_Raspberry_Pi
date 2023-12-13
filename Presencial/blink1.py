# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

def peripheral_setup():
 GPIO.setmode(GPIO.BCM) #puede cambiar a BOARD
 global led1
 led1 = 17  #si cambiar de BCM a Board defina el número del pin acorde a los pines de la raspberry
 GPIO.setup(led1, GPIO.OUT)
 
def peripheral_loop():
 GPIO.output(led1,True)
 sleep(2)
 GPIO.output(led1,False)
 sleep(2)

# Main function
def main () :

# Setup
 peripheral_setup()
 try:
# Infinite loop
  while 1 :
   peripheral_loop()
 except Exception as e:
  print()
  print("Error:", e.__class__)
  print("bye")
 except(KeyboardInterrupt):
  print()
  print("bye")
 
 GPIO.cleanup()
 
main()
