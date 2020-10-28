# From https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/

# Set positive sensor pin to pin 1
# Set data pin to 7 (GPIO4)
# Set negative pin to GND, 6

import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4     # Use data pin 4


def getTempHum():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN, retries=5, delay_seconds=0.1)

    if humidity is not None and temperature is not None:
        return (round(temperature,1), round(humidity,1) )
    else:
        return (0,0)
