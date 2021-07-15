
import RPi.GPIO as GPIO
from time import sleep
import threading

led1 = 4
led2 = 17
bt1 = 5
bt2 = 6

def int1():
 GPIO.output(led1,not(GPIO.input(led1)))
 threading.Timer(2,int1).start()
 
def int2():
 GPIO.output(led2,not(GPIO.input(led2)))
 threading.Timer(4,int2).start()
 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 threading.Timer(2,int1).start()
 threading.Timer(4,int2).start()

def peripheral_loop():
 print("hola mundo")
 sleep(2)
 
# Main function
def main () :

# Setup
 print("hola mundosssssssssssss")

 peripheral_setup()

# Infinite loop
 while 1 :
  peripheral_loop()
  pass

# Command line execution
if __name__ == '__main__' :
   main()

