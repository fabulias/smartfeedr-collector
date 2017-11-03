import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep
import sys
import os
import subprocess

flag = False
p = subprocess.Popen(['ps', '-aux'], stdout=subprocess.PIPE)
out, err = p.communicate()
for line in out.splitlines():
    file_=b'ultrasonic.py'
    if file_ in line:
        flag = True

if not flag:
    sys.exit()

portion = float(sys.argv[1]) #Asignamos las porciones ingresadas por parametro
if portion == 0:
    sys.exit()
portion=int(portion*2)
GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(12,GPIO.OUT)    #Ponemos el pin 12 como salida
p = GPIO.PWM(12,50)        #Ponemos el pin 12 en modo PWM y enviamos 50 pulsos por segundo
p.start(2.5)               #Enviamos un pulso del 2.5% para centrar el servo
try:
    for i in range(0,portion):
        p.ChangeDutyCycle(4.5)   #Enviamos un pulso del 3.75% para girar el servo hacia la izquierda
        time.sleep(1)           #pausa de medio segundo
        p.ChangeDutyCycle(2.5)   #Enviamos un pulso del 2.5% para girar el servo hacia la derecha
        time.sleep(0.5)
    GPIO.cleanup()
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
