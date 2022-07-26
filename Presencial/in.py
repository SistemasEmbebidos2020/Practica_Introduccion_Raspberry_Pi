import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
led1 = 17
GPIO.setup(led1, GPIO.OUT)

comando = input("ingresa comando ")
print(f"El comando ingresado es , {comando}")
if comando == "H":
 GPIO.output(led1,True)
else:
 GPIO.output(led1,False)
#GPIO.cleanup()
