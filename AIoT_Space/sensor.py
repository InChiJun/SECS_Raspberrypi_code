import RPi.GPIO as GPIO
import Adafruit_DHT as dht

from Set import set_gpio, set_information
from Time.time import Time, TimeCalculator
from Database.db_insert import Database

db = Database()
tc = TimeCalculator()

def add_number():
    AIoTSpace.num += 1
    return AIoTSpace.num

# 팬과 전구의 상태
class DeviceStatus:
    def __init__(self, initial_status):
        self.current_status = initial_status

    def update_status(self, new_status):
        if new_status != self.current_status:
            self.current_status = new_status

    def get_current_status(self):
        return self.current_status

class AIoTSpace:
    num = 1

    def __init__(self):
        self.fan_status = DeviceStatus(0)
        self.bulb_status = DeviceStatus(0)

    def run(self):
        timestamp = Time.nowtime(self)
        humidity, temperature = dht.read_retry(dht.DHT22, set_gpio.aiot_dht)        # 온습도 정보를 읽어온다
        aiot_ir_state = GPIO.input(set_gpio.aiot_ir)        # IR 센서의 감지 정보를 읽어온다

        if aiot_ir_state == 0:      # IR 센서에 물체가 감지되었을 때
            if self.bulb_status.get_current_status() != 1:      # 전구가 꺼져있는 상태일 때(전구 상태가 0이었을 때)
                tc.set_aiot_bulb_start_time()  # 전구가 켜진 시간을 받아온다

            add_number()
            self.bulb_status.update_status(1)       # 전구의 현재 상태를 1(켜짐)로 바꾼다
            print(timestamp, "-- Signal detected!")

            db.aiotIrInsert(AIoTSpace.num, set_information.ir2, timestamp, set_information.detect)
            GPIO.output(set_gpio.aiot_ir_bulb, GPIO.LOW)        # 전구를 작동시킨다

        elif aiot_ir_state == 1:        # IR 센서에 물체가 감지되지 않았을 때
            if self.bulb_status.get_current_status() != 0:      # 전구가 켜져있다가 꺼졌을 때(전구 상태가 1이었을 때)
                add_number()
                tc.set_aiot_bulb_stop_time()        # 전구가 꺼진 시간을 받아온다
                bulb_runtime = tc.set_aiot_bulb_runtime()       # 전구가 작동한 시간을 받아온다
                print(bulb_runtime)
                db.aiotBulbInsert(AIoTSpace.num, set_information.bulb2, bulb_runtime)
                self.bulb_status.update_status(0)       # 전구의 상태를 다시 0(꺼짐)으로 바꾼다

                add_number()
                bulb_consumption = bulb_runtime * 0.00694
                today = Time.today_day(self)
                month = Time.today_month(self)
                db.aiotConInsert(AIoTSpace.num, bulb_consumption, today, month)

            add_number()
            self.bulb_status.update_status(0)       # 전구의 현재 상태를 0(꺼짐)으로 설정한다
            print(timestamp, "-- Signal not detected!")

            db.aiotIrInsert(AIoTSpace.num, set_information.ir2, timestamp, set_information.detect)
            GPIO.output(set_gpio.aiot_ir_bulb, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temperature, humidity))

        if temperature > 30.0:
            if self.fan_status.get_current_status() != 1:
                tc.set_aiot_fan_start_time()

            add_number()
            self.fan_status.update_status(1)
            print("온도가 높으므로 쿨링팬을 작동합니다.")

            db.aiotDhtInsert(AIoTSpace.num, set_information.dht2, timestamp, temperature, humidity)
            GPIO.output(set_gpio.aiot_dht_fan, GPIO.LOW)

        elif temperature <= 30.0:
            if self.fan_status.get_current_status() != 0:
                add_number()
                tc.set_aiot_fan_stop_time()
                fan_runtime = tc.set_aiot_fan_runtime()
                db.aiotFanInsert(AIoTSpace.num, set_information.fan2, fan_runtime)
                self.fan_status.update_status(0)

                add_number()
                fan_consumption = fan_runtime * 0.72
                today = Time.today_day(self)
                month = Time.today_month(self)
                db.aiotConInsert(AIoTSpace.num, fan_consumption, today, month)

            add_number()
            self.fan_status.update_status(0)
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")

            db.aiotDhtInsert(AIoTSpace.num, set_information.dht2, timestamp, temperature, humidity)
            GPIO.output(set_gpio.aiot_dht_fan, GPIO.HIGH)