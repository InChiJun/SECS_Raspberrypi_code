import time
import RPi.GPIO as GPIO

from Set.gpioset import MySet
from IoT_Space.sensor import IoTSpace
from AIoT_Space.sensor import AIotSpace


class Controller:
    def __init__(self):
        MySet.setmode(self)
        MySet.setup(self)

    def run(self):
        while True:
            try:
                IoTSpace.run(self)
                AIotSpace.run(self)
                time.sleep(3)

            except RuntimeError as e:
                print("Reading from Sensor failure: ", e.args)

if __name__ == "__main__":
    controller = Controller()
    try:
        controller.run()
    except KeyboardInterrupt:
        GPIO.cleanup()