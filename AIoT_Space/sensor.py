import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import information

from Set import gpioset
from Time.now import Time
from db_sensor import Database

db = Database()

class AIotSpace:

    def run(self):
        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, gpioset.aiot_dht)
        aiot_ir_state = GPIO.input(gpioset.aiot_ir)

        if aiot_ir_state == 0:
            db.irInsert(information.ir2, timestamp, information.detect)
            print(Time.nowtime(self), "-- Signal detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.LOW)
        elif aiot_ir_state == 1:
            db.irInsert(information.ir2, timestamp, information.detect)
            print(Time.nowtime(self), "-- Signal not detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            db.dhtInsert(information.dht2, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.LOW)
        elif temperature <= 30.0:
            db.dhtInsert(information.dht2, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.HIGH)