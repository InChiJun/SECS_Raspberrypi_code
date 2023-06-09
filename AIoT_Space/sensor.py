import RPi.GPIO as GPIO
import Adafruit_DHT as dht

from Set import set_gpio, set_information
from Time.time import Time, TimeCalculator
from Database.db_insert import Database

db = Database()
tc = TimeCalculator()

def add_number():
    AIotSpace.num += 1
    return AIotSpace.num

class AIotSpace:
    num = 1

    def run(self):
        fan_status = 0
        fan_current_status = fan_status

        bulb_status = 0
        bulb_current_status = bulb_status

        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, set_gpio.aiot_dht)
        aiot_ir_state = GPIO.input(set_gpio.aiot_ir)

        if aiot_ir_state == 0:
            add_number()
            bulb_status = 1
            bulb_current_status = bulb_status
            tc.aiot_bulb_start_time()

            db.aiotIrInsert(AIotSpace.num, set_information.ir2, timestamp, set_information.detect)
            print(timestamp, "-- Signal detected!")
            GPIO.output(set_gpio.aiot_ir_fan, GPIO.LOW)

        elif aiot_ir_state == 1:
            add_number()
            bulb_status = 0
            if bulb_status != bulb_current_status:
                add_number()
                tc.aiot_bulb_stop_time()
                bulb_runtime = tc.aiot_bulb_runtime()
                print(bulb_runtime)
                db.aiotBulbInsert(AIotSpace.num, set_information.bulb2, bulb_runtime)
                bulb_current_status = 0

            db.aiotIrInsert(AIotSpace.num, set_information.ir2, timestamp, set_information.detect)
            print(timestamp, "-- Signal not detected!")
            GPIO.output(set_gpio.aiot_ir_fan, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            add_number()
            fan_status = 1
            fan_current_status = fan_status
            tc.aiot_fan_start_time()

            db.aiotDhtInsert(AIotSpace.num, set_information.dht2, timestamp, temperature, humidity)
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(set_gpio.aiot_dht_fan, GPIO.LOW)

        elif temperature <= 30.0:
            add_number()
            fan_status = 0
            if fan_status != fan_current_status:
                add_number()
                tc.aiot_fan_stop_time()
                fan_runtime = tc.aiot_fan_runtime()
                db.aiotFanInsert(AIotSpace.num, set_information.fan2, fan_runtime)
                fan_current_status = 0

            db.aiotDhtInsert(AIotSpace.num, set_information.dht2, timestamp, temperature, humidity)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(set_gpio.aiot_dht_fan, GPIO.HIGH)