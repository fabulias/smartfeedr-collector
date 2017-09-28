import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep
import sqlite3 

def get_porcion():
	conn = sqlite3.connect('smartfeedr.db')
	c = conn.cursor()
	c.execute("SELECT cantidad FROM porcion WHERE horario='14:00'")
	porciones =tuple(c.fetchone())
	return porciones[0]
GPIO.setmode(GPIO.BOARD)   #Ponemos la Raspberry en modo BOARD
GPIO.setup(11,GPIO.OUT)    #Ponemos el pin 12 como salida
p = GPIO.PWM(11,50)        #Ponemos el pin 12 en modo PWM y enviamos 50 pulsos por segundo
p.start(2.5)               #Enviamos un pulso del 2.5% para centrar el servo
try:
 cant=get_porcion()
 for i in range(0,cant): 
    p.ChangeDutyCycle(4.5)   #Enviamos un pulso del 3.75% para girar el servo hacia la izquierda
    time.sleep(1)           #pausa de medio segundo
    p.ChangeDutyCycle(2.5)   #Enviamos un pulso del 2.5% para girar el servo hacia la derecha  
 GPIO.cleanup()
except KeyboardInterrupt:         #Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script
