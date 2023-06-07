import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import information

from Set import gpioset
from datetime import datetime
from Time.now import Time
from db_sensor import Database

db = Database()

class IoTSpace:
    num = 1
    def addNumber(self):
        IoTSpace.num += 1
        return IoTSpace.num

    def run(self):
        fan_status = 0
        fan_start_time = ""
        fan_current_status = fan_status

        bulb_status = 0
        bulb_start_time = ""
        bulb_current_status = bulb_status

        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, gpioset.iot_dht)
        iot_ir_state = GPIO.input(gpioset.iot_ir)

        if iot_ir_state == 0:
            IoTSpace.addNumber(self)
            bulb_status = 1
            bulb_current_status = bulb_status
            bulb_start_time = timestamp

            db.iotIrInsert(IoTSpace.num, information.ir1, timestamp, information.detect)
            print(timestamp, "-- Signal detected!")
            GPIO.output(gpioset.iot_ir_fan, GPIO.LOW)
        elif iot_ir_state == 1:
            IoTSpace.addNumber(self)
            bulb_status = 0
            if bulb_status != bulb_current_status:
                IoTSpace.addNumber(self)
                bulb_stop_time = datetime.now()
                bulb_runtime = bulb_stop_time - bulb_start_time
                db.iotBulbInsert(IoTSpace.num, information.bulb1, bulb_runtime)
                bulb_current_status = 0

            db.iotIrInsert(IoTSpace.num, information.ir1, timestamp, information.non_detect)
            print(timestamp, "-- Signal not detected!")
            GPIO.output(gpioset.iot_ir_fan, GPIO.HIGH)

        print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            IoTSpace.addNumber(self)
            fan_status = 1
            fan_current_status = fan_status
            fan_start_time = timestamp

            db.iotDhtInsert(IoTSpace.num, information.dht1, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(gpioset.iot_dht_fan, GPIO.LOW)
        elif temperature <= 30.0:
            IoTSpace.addNumber(self)
            fan_status = 0
            if fan_status != fan_current_status:
                IoTSpace.addNumber(self)
                fan_stop_time = datetime.now()
                fan_runtime = fan_stop_time - fan_start_time
                db.iotFanInsert(IoTSpace.num, information.fan1, fan_runtime)
                fan_current_status = 0

            db.iotDhtInsert(IoTSpace.num, information.dht1, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(gpioset.iot_dht_fan, GPIO.HIGH)