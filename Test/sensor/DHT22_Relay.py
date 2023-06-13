# DHT22 Sensor pin = 23
import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
from datetime import datetime

dht_pin = 23
relay = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

while True:
    try:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        humidity, temperature = dht.read_retry(dht.DHT22, dht_pin)
        print("Temp={0:0.1f}*C Humidity={1:0.1f}%".format(temperature, humidity))
        
        if temperature > 22.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(relay, GPIO.HIGH)
        else:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(relay, GPIO.LOW)
            
    except RuntimeError as e:
        print("Reading from DHT failure: ", e.args)
        
    time.sleep(5)  # 5초마다 온습도를 받아온다.
        
GPIO.cleanup()
