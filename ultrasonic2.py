#!/usr/bin/python
import time
import RPi.GPIO as GPIO
from datetime import datetime
from math import fabs

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


while True:
   distance = [ReadDistance(11), ReadDistance(11), ReadDistance(11), ReadDistance(11), ReadDistance(11)]
   dist_avg = sum(distance)/float(len(distance))
   print "========================================================="
   print "Time => ", datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   print "First read"
   print "Distance to object => ",dist_avg," cm"
   time.sleep(1)
   print "Second read"
   distance2 = [ReadDistance(11),ReadDistance(11), ReadDistance(11), ReadDistance(11), ReadDistance(11)]
   dist2_avg = sum(distance2)/float(len(distance2))
   dist_real = fabs(dist2_avg - dist_avg)
   print "2 Distance to object => ", dist2_avg, " cm"
   print "List1", distance
   print "List2", distance2
   if (dist_real >= 4.0):
       print "Object detected"
       print "Descend time => ", datetime.now().strftime('%Y-%m-%d %H:%M:%S')
       time.sleep(20)
