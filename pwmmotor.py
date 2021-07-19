import RPi.GPIO as GPIO
from time import*
GPIO.setmode(GPIO.BCM)
PPWM = 12
P1 = 5
P2 = 6
GPIO.setup(PPWM, GPIO.OUT)
GPIO.setup(P1, GPIO.OUT)
GPIO.setup(P2, GPIO.OUT)
servo= GPIO.PWM(PPWM, 50) #Para crear una instancia de PWM (Canal,frecuencia)
servo.start(0) #inicilizar valor en dc del PWM
GPIO.output(P1,True)
GPIO.output(P2,False)


while True:

 for i in range(100, -1, -1):
  servo.ChangeDutyCycle(100-i) # Para cambiar el ciclo de trabajo de 0 a 100
  sleep(0.02)
 sleep(0.5)
 for i in range(100, -1, -1):
  servo.ChangeDutyCycle(i) # Para cambiar el ciclo de trabajo de 0 a 100
  sleep(0.02)
 sleep(0.5)
 GPIO.output(P1,not (GPIO.input(P1)))
 GPIO.output(P2,not (GPIO.input(P2)))
