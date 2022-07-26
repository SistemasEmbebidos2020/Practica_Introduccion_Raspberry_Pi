import sys
import RPi.GPIO as GPIO
from threading import *
from delays.delay import *
from time import *

GPIO.setwarnings(False)

led1 = 17
led2 = 27


def int1():
 state =  not(GPIO.input(led1))
 GPIO.output(led1,state)
 Timer(1,int1).start()
 
def int2():
 GPIO.output(led2,not(GPIO.input(led2)))
 Timer(3,int2).start()
 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 Timer(1,int1).start()
 Timer(3,int2).start()

def peripheral_loop():
 print("hola mundo")
 delay(2)
 #sleep(2)

# Main function
def main () :

# Setup
 print("hola mundosssssssssssss")

 peripheral_setup()
 try:
# Infinite loop
  while 1 :
   peripheral_loop()
 except : #RuntimeError :  
  Timer(1,int1)._delete() #cancel()
  print()
  print("Bye")
  sys.exit()

main()
GPIO.cleanup()
