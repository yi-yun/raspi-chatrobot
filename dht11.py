import sys
import Adafruit_DHT

def dht11():
    sensor = Adafruit_DHT.DHT11
    pin = 16

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    if (humidity is not None )and (temperature is not None):
        print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
        print("%.1f"% temperature)
        return temperature,humidity
    else:
        print('Failed to get reading. Try again!')
        sys.exit(1)
		
