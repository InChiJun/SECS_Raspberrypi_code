import RPi.GPIO as GPIO
import time

relay = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

while True:
    GPIO.output(relay, GPIO.HIGH)
    time.sleep(3)
    GPIO.output(relay, GPIO.LOW)
    time.sleep(3)

GPIO.cleanup() # GPIO를 꺼준다.
