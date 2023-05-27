import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
from datetime import datetime

class Controller:
    def __init__(self):
        self.iot_ir = 18
        self.iot_dht = 23
        self.iot_ir_fan = 2
        self.iot_dht_fan = 3
        self.aiot_ir = 24
        self.aiot_dht = 25
        self.aiot_ir_fan = 4
        self.aiot_dht_fan = 17
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.iot_ir, GPIO.IN)
        GPIO.setup(self.aiot_ir, GPIO.IN)
        GPIO.setup(self.iot_ir_fan, GPIO.OUT)
        GPIO.setup(self.iot_dht_fan, GPIO.OUT)
        GPIO.setup(self.aiot_ir_fan, GPIO.OUT)
        GPIO.setup(self.aiot_dht_fan, GPIO.OUT)
        
    def run(self):
        while True:
            try:
                now = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
                hum1, temp1 = dht.read_retry(dht.DHT22, self.iot_dht)
                hum2, temp2 = dht.read_retry(dht.DHT22, self.aiot_dht)
                iot_ir_state = GPIO.input(self.iot_ir)
                aiot_ir_state = GPIO.input(self.aiot_ir)
                
                # IoT Space
                if iot_ir_state == 0:
                    print(now, "-- Signal detected!")
                    GPIO.output(self.iot_ir_fan, GPIO.LOW)
                elif iot_ir_state == 1:
                    print(now, "-- Signal not detected!")
                    GPIO.output(self.iot_ir_fan, GPIO.HIGH)
                    
                print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temp1, hum1))
                
                if temp1 > 30.0:
                    print("온도가 높으므로 쿨링팬을 작동합니다.")
                    GPIO.output(self.iot_dht_fan, GPIO.LOW)
                elif temp1 <= 30.0:
                    print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
                    GPIO.output(self.iot_dht_fan, GPIO.HIGH)
                    
                # AIoT Space
                if aiot_ir_state == 0:
                    print(now, "-- Signal detected!")
                    GPIO.output(self.aiot_ir_fan, GPIO.LOW)
                elif aiot_ir_state == 1:
                    print(now, "-- Signal not detected!")
                    GPIO.output(self.aiot_ir_fan, GPIO.HIGH)
                    
                print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temp2, hum2))
                
                if temp2 > 30.0:
                    print("온도가 높으므로 쿨링팬을 작동합니다.")
                    GPIO.output(self.aiot_dht_fan, GPIO.LOW)
                elif temp2 <= 30.0:
                    print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
                    GPIO.output(self.aiot_dht_fan, GPIO.HIGH)
                    
                time.sleep(3)
                
            except RuntimeError as e:
                print("Reading from Sensor failure: ", e.args)
                
    def cleanup(self):
        GPIO.cleanup()
        
if __name__ == "__main__":
    controller = Controller()
    try:
        controller.run()
    except KeyboardInterrupt:
        controller.cleanup()
