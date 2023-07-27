
import RPi.GPIO as GPIO
from delays.delay import*
GPIO.setwarnings(False)

led1 = 17
led2 = 27
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
 
def peripheral_loop():
 print ("Mientras lees")
 sleep(1.5)
 #delay(1.5)
 print ("puedes presionar")
 sleep(1.5)
 #delay(1.5)
 print ("los botones que quieras")
 sleep(1.5)
 #delay(1.5)

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
  print("Bye")
  GPIO.cleanup()

main()
 
