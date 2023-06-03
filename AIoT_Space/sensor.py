import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import module_test
from Time.now import Time

class AiotSpace:

    def run(self):
        hum2, temp2 = dht.read_retry(dht.DHT22, module_test.aiot_dht)
        aiot_ir_state = GPIO.input(module_test.aiot_ir)

        if aiot_ir_state == 0:
            print(Time.nowtime(), "-- Signal detected!")
            GPIO.output(module_test.aiot_ir_fan, GPIO.LOW)
        elif aiot_ir_state == 1:
            print(Time.nowtime(), "-- Signal not detected!")
            GPIO.output(module_test.aiot_ir_fan, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temp2, hum2))

        if temp2 > 30.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(module_test.aiot_dht_fan, GPIO.LOW)
        elif temp2 <= 30.0:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(module_test.aiot_dht_fan, GPIO.HIGH)