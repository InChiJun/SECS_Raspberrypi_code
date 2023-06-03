import RPi.GPIO as GPIO

iot_ir = 18
iot_dht = 23
iot_ir_fan = 2
iot_dht_fan = 3
aiot_ir = 24
aiot_dht = 25
aiot_ir_fan = 4
aiot_dht_fan = 17

class MySet:
    def setmode(self):
        GPIO.setmode(GPIO.BCM)

    def setup(self):
        GPIO.setup(iot_ir, GPIO.IN)
        GPIO.setup(aiot_ir, GPIO.IN)
        GPIO.setup(iot_ir_fan, GPIO.OUT)
        GPIO.setup(iot_dht_fan, GPIO.OUT)
        GPIO.setup(aiot_ir_fan, GPIO.OUT)
        GPIO.setup(aiot_dht_fan, GPIO.OUT)