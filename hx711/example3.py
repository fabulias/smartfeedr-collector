import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

GPIO.setmode(GPIO.BCM)

def cleanAndExit():
    print "Cleaning..."
    GPIO.cleanup()
    print "Bye!"
    sys.exit()

hx = HX711(5,6)
hx.set_reading_format("LSB", "MSB")
#Follow steps from here:
#https://github.com/tatobari/hx711py/issues/2
#1- comment out reference unit
#2- record average value
#3- Add known weight and take another average
#4- Subtract two difference, and divide by the known weight.
#5- Apply result to "reference_unit", or 
#hx.set_reference_unit(5460.0)  #added b6+b6*(1-ave)

loop=10
counter=0
SumValue=0

hx.reset()
hx.tare(30)

for x in range (0,loop):
    val_bare = float(hx.get_weight(15))
    SumValue = SumValue+abs(val_bare)
    counter = counter+1
    print val_bare
Ave_Bare = SumValue/counter
print ('Ave_Bare:',Ave_Bare)
print "add weight"
Cal_Weight = float(raw_input('What is the weight of the Calibration piece? ' ))

counter=0
SumValue=0
for x in range (0,loop):
    val_weighted = float(hx.get_weight(15))
    SumValue = SumValue+abs(val_weighted)
    counter = counter+1
    print val_weighted
Ave_Weight = SumValue/counter
print ('Ave_Weight:',Ave_Weight)

Ref_Unit=(Ave_Weight - Ave_Bare)/Cal_Weight
print ('Ref_Unit:',Ref_Unit)

print "Remove Weight"
wait = raw_input('Hit enter when ready to proceed' )

hx.set_reference_unit(Ref_Unit)
hx.reset()
hx.tare(30)

print "put weight back on"
wait = raw_input('Hit enter when ready to proceed' )

Weight_wrong = 1;
New_Ref_Unit = Ref_Unit
print "Checking Calibration"
while Weight_wrong == 1:
    try:
        counter=0
        SumValue=0
        for x in range (0,loop):
            Weight = float(hx.get_weight(15))
            SumValue = SumValue+abs(Weight)
            counter = counter+1
            Check_Weight = SumValue/counter
            print Check_Weight, Ref_Unit, round(Weight,3),round(New_Ref_Unit,3),Cal_Weight,round(Check_Weight,3)

        if (Cal_Weight > (Check_Weight*(0.998))) and (Cal_Weight < (Check_Weight*(1.002))):
            Weight_wrong = 0
            break
        else:
            New_Ref_Unit = Ref_Unit + (Ref_Unit*(1-(Cal_Weight/Check_Weight)))/2
            print ('New_Ref_Weight:',round(New_Ref_Unit,3),Cal_Weight,round(Check_Weight,3))

        wait = raw_input('Remove Weight, Hit enter when ready to proceed' )
        hx.set_reference_unit(New_Ref_Unit)
        hx.reset()
        hx.tare(5)
        wait = raw_input('Add Weight, Hit enter when ready to proceed' )

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

Ref_Unit = New_Ref_Unit

cleanAndExit()
#code source : https://github.com/tatobari/hx711py/blob/master/example.py
