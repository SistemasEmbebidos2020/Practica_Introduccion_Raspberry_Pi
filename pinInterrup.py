
import RPi.GPIO as GPIO
from delay import*

led1 = 2
led2 = 3
bt1 = 14
bt2 = 15

def my_callback1(self):
 GPIO.output(led1,not(GPIO.input(led1)))

def my_callback2(self):
 GPIO.output(led2,not(GPIO.input(led2)))

 
def peripheral_setup():
 GPIO.setmode(GPIO.BCM)
 GPIO.setup(led1, GPIO.OUT)
 GPIO.setup(led2, GPIO.OUT)
 GPIO.setup(bt1, GPIO.IN, GPIO.PUD_DOWN)
 GPIO.setup(bt2, GPIO.IN, GPIO.PUD_UP)
 GPIO.add_event_detect(bt1,GPIO.FALLING,callback=my_callback1,bouncetime=300)
 GPIO.add_event_detect(bt2,GPIO.RISING,callback=my_callback2,bouncetime=300)
 
# Main function
def main () :
# Setup
 peripheral_setup()
try:
# Infinite loop
 while 1 :
  peripheral_loop()
  print ("Mientras lees")
  delay(1.5)
  print ("puedes presionar")
  delay(1.5)
  print ("los botones que quieras")
  delay(1.5)
except:
 print()
 print("Bye")
 GPIO.cleanup()
# Command line execution
if __name__ == '__main__' :
   main()
 
