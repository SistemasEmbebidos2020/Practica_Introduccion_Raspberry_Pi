import RPi.GPIO as GPIO
from time import*

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

PPWM = 12
GPIO.setup(PPWM, GPIO.OUT)
led= GPIO.PWM(PPWM, 50) #Para crear una instancia de PWM (Canal,frecuencia)
led.start(0) #inicilizar valor en dc del PWM
t=0
try:
 while True:
  while t < 100:
   led.ChangeDutyCycle(t) # Para cambiar el ciclo de trabajo de 0 a 100
   t+=5
   sleep(0.2)
  while t > 0:
   led.ChangeDutyCycle(t) # Para cambiar el ciclo de trabajo de 0 a 100
   t-=5
   sleep(0.2)
except:
 print()
 print("Bye")
 GPIO.cleanup()
