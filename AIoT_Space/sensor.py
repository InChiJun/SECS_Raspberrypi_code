import RPi.GPIO as GPIO
import Adafruit_DHT as dht

from Set import gpioset
from Time.now import Time

class AiotSpace:

    def run(self):
        hum2, temp2 = dht.read_retry(dht.DHT22, gpioset.aiot_dht)
        aiot_ir_state = GPIO.input(gpioset.aiot_ir)

        if aiot_ir_state == 0:
            print(Time.nowtime(self), "-- Signal detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.LOW)
        elif aiot_ir_state == 1:
            print(Time.nowtime(self), "-- Signal not detected!")
            GPIO.output(gpioset.aiot_ir_fan, GPIO.HIGH)

        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temp2, hum2))

        if temp2 > 30.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.LOW)
        elif temp2 <= 30.0:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(gpioset.aiot_dht_fan, GPIO.HIGH)