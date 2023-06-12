import time
import RPi.GPIO as GPIO

from Set.set_gpio import MySet
from IoT_Space.sensor import IoTSpace
from AIoT_Space.sensor import AIoTSpace
from Time.time import TimeCalculator


class Controller:
    def __init__(self):
        MySet.setmode(self)
        MySet.setup(self)
        self.iot_space = IoTSpace()
        self.aiot_space = AIoTSpace()
        self.tc = TimeCalculator()

    def run(self):
        while True:
            try:
                self.iot_space.run()
                self.aiot_space.run()
                time.sleep(3)

            except RuntimeError as e:
                print("Reading from Sensor failure: ", e.args)

if __name__ == "__main__":
    controller = Controller()
    try:
        controller.run()
    except KeyboardInterrupt:
        GPIO.cleanup()
