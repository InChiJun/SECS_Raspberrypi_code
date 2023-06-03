from datetime import datetime

class Time:

    def nowtime(self):
        now = datetime.now().strftime('%Y:%m:%d %H:%M:%S')
        return now