# DHT22 Sensor pin = 23
import time
import Adafruit_DHT as dht

while True:
    try:
        humidity, temperature = dht.read_retry(dht.DHT22, 23)
        print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
        
    time.sleep(0.5)
