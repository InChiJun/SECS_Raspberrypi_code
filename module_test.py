import time

from Set.gpioset import MySet
from IoT_Space import sensor
from AIoT_Space import sensor

iot_ir = 18
iot_dht = 23
iot_ir_fan = 2
iot_dht_fan = 3
aiot_ir = 24
aiot_dht = 25
aiot_ir_fan = 4
aiot_dht_fan = 17

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