import time

from Set.gpioset import MySet
from IoT_Space.sensor import IotSpace
from AIoT_Space.sensor import AiotSpace


class Controller:
    def __init__(self):
        MySet.setmode(self)
        MySet.setup(self)

    def run(self):
        while True:
            try:
                IotSpace.run()
                AiotSpace.run()
                time.sleep(3)

            except RuntimeError as e:
                print("Reading from Sensor failure: ", e.args)

if __name__ == "__main__":
    controller = Controller()
    try:
        controller.run()
    except KeyboardInterrupt:
        MySet.cleanup()