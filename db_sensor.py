import pymysql
import my_db
import information

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
    def iotDhtInsert(self, name, timestamp, temperature, humidity):
        sql = information.iot_dht_sql
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()

    # iot_space 적외선 센서의 상태 Insert
    def iotIrInsert(self, name, timestamp, status):
        sql = information.iot_ir_sql
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()

    # iot_space 쿨링팬의 상태 Insert
    def iotFanInsert(self, name, runtime):
        sql = information.iot_fan_sql
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()

    # iot_space 전구의 상태 Insert
    def iotBulbInsert(self, name, runtime):
        sql = information.iot_bulb_sql
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()

    # aiot_space 온습도 센서의 상태 Insert
    def aiotDhtInsert(self, name, timestamp, temperature, humidity):
        sql = information.aiot_dht_sql
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()

    # aiot_space 적외선 센서의 상태 Insert
    def aiotIrInsert(self, name, timestamp, status):
        sql = information.aiot_ir_sql
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()

    # aiot_space 쿨링팬의 상태 Insert
    def aiotFanInsert(self, name, runtime):
        sql = information.aiot_fan_sql
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()

    # aiot_space 전구의 상태 Insert
    def aiotBulbInsert(self, name, runtime):
        sql = information.aiot_bulb_sql
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()