import RPi.GPIO as GPIO
import module_test


class Gpio:
    def setmode(self):
        GPIO.setmode(GPIO.BCM)

    def setup(self):
        GPIO.setup(module_test.iot_ir, GPIO.IN)
        GPIO.setup(module_test.aiot_ir, GPIO.IN)
        GPIO.setup(module_test.iot_ir_fan, GPIO.OUT)
        GPIO.setup(module_test.iot_dht_fan, GPIO.OUT)
        GPIO.setup(module_test.aiot_ir_fan, GPIO.OUT)
        GPIO.setup(module_test.aiot_dht_fan, GPIO.OUT)

    def cleanup(self):
        GPIO.cleanup()