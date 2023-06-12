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

    # iot_space 온습도 센서의 상태 Insert
    def iotDhtInsert(self, id, name, timestamp, temperature, humidity):
        sql = set_information.iot_dht_sql
        self.cursor.execute(sql, (id, name, timestamp, temperature, humidity))
        self.db.commit()

    # iot_space 적외선 센서의 상태 Insert
    def iotIrInsert(self, id, name, timestamp, status):
        sql = set_information.iot_ir_sql
        self.cursor.execute(sql, (id, name, timestamp, status))
        self.db.commit()

    # iot_space 쿨링팬의 상태 Insert
    def iotFanInsert(self, id, name, runtime):
        sql = set_information.iot_fan_sql
        self.cursor.execute(sql, (id, name, runtime))
        self.db.commit()

    # iot_space 전구의 상태 Insert
    def iotBulbInsert(self, id, name, runtime):
        sql = set_information.iot_bulb_sql
        self.cursor.execute(sql, (id, name, runtime))
        self.db.commit()

    def iotConInsert(self, id, consumption, daily, month):
        sql = set_information.iot_con_sql
        self.cursor.execute(sql, (id, consumption, daily, month))
        self.db.commit()

    # aiot_space 온습도 센서의 상태 Insert
    def aiotDhtInsert(self, id, name, timestamp, temperature, humidity):
        sql = set_information.aiot_dht_sql
        self.cursor.execute(sql, (id, name, timestamp, temperature, humidity))
        self.db.commit()

    # aiot_space 적외선 센서의 상태 Insert
    def aiotIrInsert(self, id, name, timestamp, status):
        sql = set_information.aiot_ir_sql
        self.cursor.execute(sql, (id, name, timestamp, status))
        self.db.commit()

    # aiot_space 쿨링팬의 상태 Insert
    def aiotFanInsert(self, id, name, runtime):
        sql = set_information.aiot_fan_sql
        self.cursor.execute(sql, (id, name, runtime))
        self.db.commit()

    # aiot_space 전구의 상태 Insert
    def aiotBulbInsert(self, id, name, runtime):
        sql = set_information.aiot_bulb_sql
        self.cursor.execute(sql, (id, name, runtime))
        self.db.commit()

    def aiotConInsert(self, id, consumption, daily, month):
        sql = set_information.aiot_con_sql
        self.cursor.execute(sql, (id, consumption, daily, month))
        self.db.commit()