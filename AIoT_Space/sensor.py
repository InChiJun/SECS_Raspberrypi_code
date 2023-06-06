import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import information

from Set import gpioset
from datetime import datetime
from Time.now import Time
from db_sensor import Database

db = Database()

class AIotSpace:
    num = 1

    def run(self):
        fan_status = 0
        fan_start_time = ""
        fan_current_status = fan_status

        bulb_status = 0
        bulb_start_time = ""
        bulb_current_status = bulb_status

        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, gpioset.aiot_dht)
        aiot_ir_state = GPIO.input(gpioset.aiot_ir)

        if aiot_ir_state == 0:
            AIotSpace.num += 1
            bulb_status = 1
            bulb_current_status = bulb_status
            bulb_start_time = timestamp

            db.aiotIrInsert(AIotSpace.num, information.ir2, timestamp, information.detect)
            print(Time.nowtime(self), "-- Signal detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.LOW)
        elif aiot_ir_state == 1:
            AIotSpace.num += 1
            bulb_status = 0
            if bulb_status != bulb_current_status:
                AIotSpace.num += 1
                bulb_stop_time = datetime.now()
                bulb_runtime = bulb_stop_time - bulb_start_time
                db.aiotBulbInsert(AIotSpace.num, information.bulb2, bulb_runtime)
                bulb_current_status = 0

            db.aiotIrInsert(AIotSpace.num, information.ir2, timestamp, information.detect)
            print(Time.nowtime(self), "-- Signal not detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            AIotSpace.num += 1
            fan_status = 1
            fan_current_status = fan_status
            fan_start_time = timestamp

            db.aiotDhtInsert(AIotSpace.num, information.dht2, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.LOW)
        elif temperature <= 30.0:
            AIotSpace.num += 1
            fan_status = 0
            if fan_status != fan_current_status:
                AIotSpace.num += 1
                fan_stop_time = datetime.now()
                fan_runtime = fan_stop_time - fan_start_time
                db.aiotFanInsert(AIotSpace.num, information.fan2, fan_runtime)
                fan_current_status = 0

            db.aiotDhtInsert(AIotSpace.num, information.dht2, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.HIGH)