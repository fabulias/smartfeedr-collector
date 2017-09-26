import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep

GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(12,GPIO.OUT)    #Ponemos el pin 12 como salida
p = GPIO.PWM(12,50)        #Ponemos el pin 12 en modo PWM y enviamos 50 pulsos por segundo
p.start(2.5)               #Enviamos un pulso del 2.5% para centrar el servo

try:
    p.ChangeDutyCycle(3.75)    #Enviamos un pulso del 3.75% para girar el servo hacia la izquierda
    time.sleep(0.5)           #pausa de medio segundo
    p.ChangeDutyCycle(2.5)   #Enviamos un pulso del 2.5% para girar el servo hacia la derecha
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
