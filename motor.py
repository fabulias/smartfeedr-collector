# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO 
import time 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

freq = float(80) #freq -> frequency
period = 1000/freq #1000 ms = 1 s esto nos  dice cuanto demora en girar 360º
#El pulso indica cuanto durará el movimiento, ej: 360->periodo s ; xº->pulso        
pulso=0.5  #pulso 0.5 ms genera 0ª
#duty cycle
dc = (pulso/period)*100
pwm = GPIO.PWM(11,freq)
print "dc -> ", dc
pwm.start(dc)

try:
	ix = dc
	while True:
		pwm.ChangeDutyCycle(ix) #80 degree
		ix = ix + 4
		time.sleep(1)
                print "->", ix
#		pwm.ChangeDutyCycle(12) #90 degree
#		time.sleep(1)
#		print "3"
#		pwm.ChangeDutyCycle(50) #0 degree
#		time.sleep(1)
		#pwm.ChangeDutyCycle(50) #180 degree
		#time.sleep(1)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()

