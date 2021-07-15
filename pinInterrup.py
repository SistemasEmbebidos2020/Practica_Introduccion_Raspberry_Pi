
import RPi.GPIO as GPIO
from time import*

led1 = 4
led2 = 17
bt1 = 5
bt2 = 6

def my_callback1():
 GPIO.output(led1,not(GPIO.input(led1)))

def my_callback2():
 GPIO.output(led2,not(GPIO.input(led2)))

 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 GPIO.setup(bt1, GPIO.IN, GPIO.PUD_DOWN)
 GPIO.setup(bt2, GPIO.IN, GPIO.PUD_UP)
 GPIO.add_event_detect(bt1,GPIO.FALLING,callback=my_callback1,bouncetime=300)
 GPIO.add_event_detect(bt2,GPIO.RISING,callback=my_callback2,bouncetime=300)

def mysleep(delay): 
 start = time() 
 while time()-start < delay:
  pass


def peripheral_loop():
 pass
 
# Main function
def main () :

# Setup
 peripheral_setup()

# Infinite loop
 while 1 :
  peripheral_loop()
  print ("hola")
  mysleep(5)
  print ("mnmnma")
  mysleep(5)
  print ("timepo")
  mysleep(5)
  pass
  pass

# Command line execution
if __name__ == '__main__' :
   main()

