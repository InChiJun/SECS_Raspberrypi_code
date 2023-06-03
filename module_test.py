import time

from Set.gpioset import MySet
from IoT_Space import sensor
from AIoT_Space import sensor


class Controller:
    def __init__(self):
        MySet.setmode()
        MySet.setup()

    def run(self):
        while True:
            try:
                sensor.IotSpace.run()
                sensor.AiotSpace.run()
                time.sleep(3)

            except RuntimeError as e:
                print("Reading from Sensor failure: ", e.args)

if __name__ == "__main__":
    controller = Controller()
    try:
        controller.run()
    except KeyboardInterrupt:
        MySet.cleanup()