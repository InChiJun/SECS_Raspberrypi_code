# IR sensor pin = 23, Relay module pin = 18
import RPi.GPIO as GPIO
import time
from datetime import datetime

ir = 24
relay = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(ir, GPIO.IN)
GPIO.setup(relay, GPIO.OUT)

while True:
    try:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        ir_state = GPIO.input(ir)
        
        if ir_state == 0:  # 신호가 감지되면 1=True=GPIO.HIGH값으로 Signal detected가 출력되어야 하나 반대로 인식됨에 따라 0으로 작성
            print(now, "-- Signal detected!")
            GPIO.output(relay, GPIO.LOW)
            
        else:
            print(now, "-- Signal not detected!")
            GPIO.output(relay, GPIO.HIGH)
            
        time.sleep(3)  # 5초마다 감지된 신호를 읽어오기 위함. 적외선이 감지되면 팬이 5초동안 돌아가며 그동안은 꺼지지 않음.
            
    except RuntimeError as e:
        print("Reading from IR failure: ", e.args)

GPIO.cleanup()  # GPIO를 초기화시킴. 핀 항시 사용을 막기 위함.
