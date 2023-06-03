import pymysql

class Database():
    def __init__(self):
        self.db = pymysql.connect(host='localhost', port=3306, user='root',password=my_db.password, db='sensor_data', charset='utf8')
        self.cursor = self.db.cursor()
        
    def dhtInsert(self, name, timestamp, temperature, humidity):
        sql = """insert into sensor values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, temperature, humidity))
        self.db.commit()
        
    def irInsert(self, name, timestamp, status):
        sql = """insert into sensor values (%s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, status))
        self.db.commit()
        
    def fanInsert(self, name, timestamp, status, runtime):
        sql = """insert into sensor values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, status, runtime))
        self.db.commit()
        
    def bulbInsert(self, name, timestamp, status, runtime):
        sql = """insert into sensor values (%s, %s, %s, %s)"""
        self.cursor.execute(sql, (name, timestamp, status, runtime))
        self.db.commit()
