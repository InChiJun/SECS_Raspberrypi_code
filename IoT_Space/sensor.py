import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import information

from Set import gpioset
from Time.now import Time
from db_sensor import Database

db = Database()

class IotSpace:

    def run(self):
        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, gpioset.iot_dht)
        iot_ir_state = GPIO.input(gpioset.iot_ir)

        if iot_ir_state == 0:
            db.irInsert(information.ir1, timestamp, information.detect)
            print(timestamp, "-- Signal detected!")
            GPIO.output(gpioset.iot_ir_fan, GPIO.LOW)
        elif iot_ir_state == 1:
            db.irInsert(information.ir1, timestamp, information.non_detect)
            print(timestamp, "-- Signal not detected!")
            GPIO.output(gpioset.iot_ir_fan, GPIO.HIGH)

        print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            db.dhtInsert(information.dht1, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(gpioset.iot_dht_fan, GPIO.LOW)
        elif temperature <= 30.0:
            db.dhtInsert(information.dht1, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(gpioset.iot_dht_fan, GPIO.HIGH)