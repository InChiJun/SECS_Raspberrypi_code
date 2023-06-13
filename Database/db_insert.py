import pymysql
import my_db
from Set import set_information


class Database:
    def __init__(self):
        self.db = pymysql.connect(host=my_db.host,
                                  port=3306,
                                  user='root',
                                  password=my_db.password,
                                  db='SECS',
                                  charset='utf8')
        self.cursor = self.db.cursor()

    # iot_space 온습도 센서
    def iotDhtInsert(self, name, timestamp, temperature, humidity):
        sql = set_information.iot_dht_sql
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()

    # iot_space 적외선 센서
    def iotIrInsert(self, name, timestamp, status):
        sql = set_information.iot_ir_sql
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()

    # iot_space 쿨링팬
    def iotFanInsert(self, name, runtime, fan_consumption, daily, month):
        sql = set_information.iot_fan_sql
        self.cursor.execute(sql, (name, runtime, fan_consumption, daily, month))
        self.db.commit()

    # iot_space 전구
    def iotBulbInsert(self, name, runtime, bulb_consumption, daily, month):
        sql = set_information.iot_bulb_sql
        self.cursor.execute(sql, (name, runtime, bulb_consumption, daily, month))
        self.db.commit()

    # iot_space 일월별 전력소비량
    def iotConInsert(self):
        self.cursor.execute("select daily, sum(fan_consumption) from iot_space_fan group by  daily")
        result = self.cursor.fetchall()
        for row in result:
            fan_consumption = row[1]
            self.cursor.execute("update iot_space_consumption set daily_consumption = ?", (fan_consumption, ))
        self.cursor.execute("select daily, sum(bulb_consumption) from iot_space_bulb group by  daily")
        result = self.cursor.fetchall()
        for row in result:
            bulb_consumption = row[1]
            self.cursor.execute("update iot_space_consumption set daily_consumption = ?", (bulb_consumption, ))
        self.db.commit()

    # aiot_space 온습도 센서
    def aiotDhtInsert(self, name, timestamp, temperature, humidity):
        sql = set_information.aiot_dht_sql
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()

    # aiot_space 적외선 센서
    def aiotIrInsert(self, name, timestamp, status):
        sql = set_information.aiot_ir_sql
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()

    # aiot_space 쿨링팬
    def aiotFanInsert(self, name, runtime, fan_consumption, daily, month):
        sql = set_information.aiot_fan_sql
        self.cursor.execute(sql, (name, runtime, fan_consumption, daily, month))
        self.db.commit()

    # aiot_space 전구
    def aiotBulbInsert(self, name, runtime, bulb_consumption, daily, month):
        sql = set_information.aiot_bulb_sql
        self.cursor.execute(sql, (name, runtime, bulb_consumption, daily, month))
        self.db.commit()

    # aiot_space 일월별 전력소비량
    def aiotConInsert(self, daily_consumption, monthly_consumption):
        sql = set_information.aiot_con_sql
        self.cursor.execute(sql, (daily_consumption, monthly_consumption))
        self.db.commit()