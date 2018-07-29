import RPi.GPIO as GPIO
pin=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)
def on():
    GPIO.output(pin,True)
    
def off():
    GPIO.output(pin,False)