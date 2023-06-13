import RPi.GPIO as GPIO
import Adafruit_DHT as dht
import time
from datetime import datetime

fan1 = 2   # IN1 - LED로 변경 예정
fan2 = 3   # IN2
fan3 = 4   # IN3 - LED로 변경 예정
fan4 = 17  # IN4
ir1 = 18
dht1_pin = 23
ir2 = 24
dht2_pin = 25

GPIO.setmode(GPIO.BCM)

GPIO.setup(ir1, GPIO.IN)
GPIO.setup(ir2, GPIO.IN)
GPIO.setup(fan1, GPIO.OUT)
GPIO.setup(fan2, GPIO.OUT)
GPIO.setup(fan3, GPIO.OUT)
GPIO.setup(fan4, GPIO.OUT)


while True:
    try:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        hum1, temp1 = dht.read_retry(dht.DHT22, dht1_pin)
        hum2, temp2 = dht.read_retry(dht.DHT22, dht2_pin)
        ir_state1 = GPIO.input(ir1)
        ir_state2 = GPIO.input(ir2)
        
        # IoT Space
        if ir_state1 == 0:
            print(now, "-- Signal detected!")
            GPIO.output(fan1, GPIO.LOW)
            
        elif ir_state1 == 1:
            print(now, "-- Signal not detected!")
            GPIO.output(fan1, GPIO.HIGH)
            
        print("Temp1={0:0.1f}*C Humidity1={1:0.1f}%".format(temp1, hum1))
        
        if temp1 > 30.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(fan2, GPIO.LOW)
        elif temp1 <= 30.0:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(fan2, GPIO.HIGH)
            
        # AIoT Space
        if ir_state2 == 0:
            print(now, "-- Signal detected!")
            GPIO.output(fan3, GPIO.LOW)
            
        elif ir_state2 == 1:
            print(now, "-- Signal not detected!")
            GPIO.output(fan3, GPIO.HIGH)
            
        print("Temp2={0:0.1f}*C Humidity2={1:0.1f}%".format(temp2, hum2))
            
        if temp2 > 30.0:
            print("온도가 높으므로 쿨링팬을 작동합니다.")
            GPIO.output(fan4, GPIO.LOW)
        elif temp2 <= 30.0:
            print("온도가 낮으므로 쿨링팬이 작동하지 않습니다.")
            GPIO.output(fan4, GPIO.HIGH)
            
        time.sleep(3)
            
    except RuntimeError as e:
        print("Reading from Sensor failure: ", e.args)

GPIO.cleanup()
