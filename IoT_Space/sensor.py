import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import module_test
from Time.now import Time

class IotSpace:

    def run(self):
        hum1, temp1 = dht.read_retry(dht.DHT22, module_test.iot_dht)
        iot_ir_state = GPIO.input(module_test.iot_ir)

        if iot_ir_state == 0:
            print(Time.nowtime(), "-- Signal detected!")
            GPIO.output(module_test.iot_ir_fan, GPIO.LOW)
        elif iot_ir_state == 1:
            print(Time.nowtime(), "-- Signal not detected!")
            GPIO.output(module_test.iot_ir_fan, GPIO.HIGH)

        print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temp1, hum1))

        if temp1 > 30.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(module_test.iot_dht_fan, GPIO.LOW)
        elif temp1 <= 30.0:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(module_test.iot_dht_fan, GPIO.HIGH)