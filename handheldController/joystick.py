from machine import Pin, ADC
import utime

"""
Note there are only three pins that have an adc on the rpi pico

gnd -> gnd
3.3out -> +5v
32/ADC1 -> VRx
33/ADC2 -> VRy
22/GP17 -> sw

"""

xAxis = ADC(Pin(27)) #GP 27 not pin 27 
yAxis = ADC(Pin(26)) #GP 26 not hole 26
button = Pin(17,Pin.IN, Pin.PULL_UP)

while True:
    xValue = xAxis.read_u16()
    yValue = yAxis.read_u16()
    buttonValue = button.value()
    buttonStatus = "not pressed"


    if buttonValue == 0:
        buttonStatus = "pressed"
        
        
    print("X: " + str(xValue) + ", Y: " + str(yValue) + " -- button value: " + str(buttonValue) + " button status: " + buttonStatus)
    utime.sleep(0.2)