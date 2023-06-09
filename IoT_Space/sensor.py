import RPi.GPIO as GPIO
import Adafruit_DHT as dht

from Set import set_gpio, set_information
from Time.time import Time, TimeCalculator
from Database.db_insert import Database

db = Database()
tc = TimeCalculator()

def add_number():
    IoTSpace.num += 1
    return IoTSpace.num

class IoTSpace:
    num = 1

    def run(self):
        fan_status = 0
        fan_current_status = fan_status

        bulb_status = 0
        bulb_current_status = bulb_status

        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, set_gpio.iot_dht)
        iot_ir_state = GPIO.input(set_gpio.iot_ir)

        if iot_ir_state == 0:
            add_number()
            bulb_status = 1
            bulb_current_status = bulb_status
            tc.iot_bulb_start_time()

            db.iotIrInsert(IoTSpace.num, set_information.ir1, timestamp, set_information.detect)
            print(timestamp, "-- Signal detected!")
            GPIO.output(set_gpio.iot_ir_fan, GPIO.LOW)

        elif iot_ir_state == 1:
            add_number()
            bulb_status = 0
            if bulb_status != bulb_current_status:
                add_number()
                tc.iot_bulb_stop_time()
                bulb_runtime = tc.iot_bulb_runtime()
                print(bulb_runtime)
                db.iotBulbInsert(IoTSpace.num, set_information.bulb1, bulb_runtime)
                bulb_current_status = 0

            db.iotIrInsert(IoTSpace.num, set_information.ir1, timestamp, set_information.non_detect)
            print(timestamp, "-- Signal not detected!")
            GPIO.output(set_gpio.iot_ir_fan, GPIO.HIGH)

        print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            add_number()
            fan_status = 1
            fan_current_status = fan_status
            tc.iot_fan_start_time()

            db.iotDhtInsert(IoTSpace.num, set_information.dht1, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(set_gpio.iot_dht_fan, GPIO.LOW)

        elif temperature <= 30.0:
            add_number()
            fan_status = 0
            if fan_status != fan_current_status:
                add_number()
                tc.iot_fan_stop_time()
                fan_runtime = tc.iot_fan_runtime()
                db.iotFanInsert(IoTSpace.num, set_information.fan1, fan_runtime)
                fan_current_status = 0

            db.iotDhtInsert(IoTSpace.num, set_information.dht1, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(set_gpio.iot_dht_fan, GPIO.HIGH)