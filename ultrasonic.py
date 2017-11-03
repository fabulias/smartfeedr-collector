#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from datetime import datetime
from math import fabs
import os

# Use board based pin numbering
GPIO.setmode(GPIO.BOARD)


def ReadDistance(pin):
   GPIO.setup(pin, GPIO.OUT)
   GPIO.output(pin, 0)

   time.sleep(0.000002)


   #send trigger signal
   GPIO.output(pin, 1)


   time.sleep(0.000005)


   GPIO.output(pin, 0)


   GPIO.setup(pin, GPIO.IN)


   while GPIO.input(pin)==0:
      starttime=time.time()


   while GPIO.input(pin)==1:
      endtime=time.time()

   duration=endtime-starttime
   # Distance is defined as time/2 (there and back) * speed of sound 34000 cm/s
   distance=duration*34000/2
   return distance

print ("ultrasonic code is running...")
while True:
   distance = 15
   time.sleep(1)
   distance2 = ReadDistance(11)
   if distance2 > 15:
       continue
   dist_real = fabs(distance2 - distance)
   time.sleep(0.1)
   if (dist_real >= 3.0):
       print ("Object detected")
       print ("Descend time => ", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       time.sleep(20)
