from datetime import datetime

class Time:
    def nowtime(self):
        now = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
        return now

class TimeCalculator:
    def __init__(self):
        self.iot_bulb_start_time = None
        self.iot_bulb_stop_time = None

        self.iot_fan_start_time = None
        self.iot_fan_stop_time = None

        self.aiot_bulb_start_time = None
        self.aiot_bulb_stop_time = None

        self.aiot_fan_start_time = None
        self.aiot_fan_stop_time = None

    def iot_bulb_start_time(self):
        self.iot_bulb_start_time = datetime.now()

    def iot_bulb_stop_time(self):
        self.iot_bulb_stop_time = datetime.now()

    def iot_bulb_runtime(self):
        time_difference = self.iot_bulb_stop_time - self.iot_bulb_start_time
        runtime = time_difference.total_seconds()
        return runtime

    def iot_fan_start_time(self):
        self.iot_fan_start_time = datetime.now()

    def iot_fan_stop_time(self):
        self.iot_fan_stop_time = datetime.now()

    def iot_fan_runtime(self):
        time_difference = self.iot_fan_stop_time - self.iot_fan_start_time
        runtime = time_difference.total_seconds()
        return runtime

    def aiot_bulb_start_time(self):
        self.aiot_bulb_start_time = datetime.now()

    def aiot_bulb_stop_time(self):
        self.aiot_bulb_stop_time = datetime.now()

    def aiot_bulb_runtime(self):
        time_difference = self.aiot_bulb_stop_time - self.aiot_bulb_start_time
        runtime = time_difference.total_seconds()
        return runtime

    def aiot_fan_start_time(self):
        self.aiot_fan_start_time = datetime.now()

    def aiot_fan_stop_time(self):
        self.aiot_fan_stop_time = datetime.now()

    def aiot_fan_runtime(self):
        time_difference = self.aiot_fan_stop_time - self.aiot_fan_start_time
        runtime = time_difference.total_seconds()
        return runtime