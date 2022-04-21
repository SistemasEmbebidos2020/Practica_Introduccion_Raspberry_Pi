import RPi.GPIO as GPIO
from time import*

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

PPWM = 12
GPIO.setup(PPWM, GPIO.OUT)
servo= GPIO.PWM(PPWM, 50) #Para crear una instancia de PWM (Canal,frecuencia)
servo.start(0) #inicilizar valor en dc del PWM

try:
 while True:
  servo.ChangeDutyCycle(25) # Para cambiar el ciclo de trabajo de 0 a 100
  sleep(0.02)
except:
 print()
 print("Bye")
 GPIO.cleanup()
