
import RPi.GPIO as GPIO
from delay import *
from threading import *

GPIO.setwarnings(False)

led1 = 2
led2 = 3
bt1 = 14
bt2 = 15

def int1():
 GPIO.output(led1,not(GPIO.input(led1)))
 Timer(2,int1).start()
 
def int2():
 GPIO.output(led2,not(GPIO.input(led2)))
 Timer(4,int2).start()
 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 Timer(2,int1).start()
 Timer(4,int2).start()

def peripheral_loop():
 print("hola mundo")
 delay(2)
 
# Main function
def main () :

# Setup
 print("hola mundosssssssssssss")

 peripheral_setup()
 try:
# Infinite loop
  while 1 :
   peripheral_loop()
 except:
  print()
  print("Bye")
  GPIO.cleaup()
# Command line execution
if __name__ == '__main__' :
   main()

