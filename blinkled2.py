
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

led1 = 4
led2 = 17
bt1 = 5
bt2 = 6

def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(bt1, GPIO.IN, GPIO.PUD_DOWN)
 GPIO.setup(led2, GPIO.OUT)
 GPIO.setup(bt2, GPIO.IN, GPIO.PUD_UP)

def peripheral_loop():
 if GPIO.input(bt1):
  GPIO.output(led1,True)
 else:
  GPIO.output(led1,False)
 if GPIO.input(bt2):
  GPIO.output(led2,False)
 else:
  GPIO.output(led2,True)

 
# Main function
def main () :
 
 # Setup
 peripheral_setup()
 try:
 # Infinite loop
  while 1 :
   peripheral_loop()
 except:
  print()
  print("bye")
  GPIO.cleanup()
 
# Command line execution
if __name__ == '__main__' :
   main()

