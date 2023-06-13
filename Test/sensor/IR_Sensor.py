import RPi.GPIO as GPIO
from datetime import datetime
import time

ir_pin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir_pin, GPIO.IN)

while True:
    try:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ir_state = GPIO.input(ir_pin)
        
        if ir_state == 0:  # 신호가 감지되면 True=GPIO.HIGH값으로 Signal detected가 출력되어야 하나 반대로 인식됨
            print(now, "-- Signal detected!")
        else:
            print(now, "-- Signal not detected!")
            
        time.sleep(0.5)
    except RuntimeError as e:
        print("Reading from IR failure: ", e.args)

GPIO.cleanup()
