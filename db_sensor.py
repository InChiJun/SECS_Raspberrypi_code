import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root',password=my_db.password, db='sensor_data', charset='utf8')
        self.cursor = self.db.cursor()

    # 온습도 센서의 상태 Insert
    def dhtInsert(self, name, timestamp, temperature, humidity):
        sql = """insert into sensor values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()

    # 적외선 센서의 상태 Insert
    def irInsert(self, name, timestamp, status):
        sql = """insert into sensor values (%s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()

    # 쿨링팬의 상태 Insert
    def fanInsert(self, name, runtime):
        sql = """insert into sensor values (%s, %s)"""
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()

    # 전구의 상태 Insert
    def bulbInsert(self, name, runtime):
        sql = """insert into sensor values (%s, %s)"""
        self.cursor.execute(sql, (name, runtime))
        self.db.commit()
