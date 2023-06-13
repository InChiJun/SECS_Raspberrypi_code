from random import *
import time
import pymysql
from Database import my_db

count = 0
sensor_value = 0
index = 1
while(1):
    i = randint(100,999)
    sensor_value=sensor_value+i
    time.sleep(1)
    count=count+1
    
    if count==5:
        conn = pymysql.Connect(host=my_db.host, user='root', password=my_db.password, db='sensor_data', charset='utf8')
        curr = conn.cursor()
        res = sensor_value/5
        
        sql = "insert into value1 values(' " + str(index) +" ', '" + my_db.host + "',' " + str(res) + " ')"
        print(sql)
        print(curr.execute(sql))
        conn.commit()
        count=0
        sensor_value=0
        index += 1
        curr.close()
        conn.close()
        conn = None
        curr = None
