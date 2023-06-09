# sensor
dht1 = 'IoT_DHT22_1'
ir1 = 'IoT_IR_1'
dht2 = 'AIoT_DHT22_1'
ir2 = 'AIoT_IR_1'

# equipment
fan1 = 'IoT_Fan_1'
bulb1 = 'IoT_Bulb_1'
fan2 = 'AIoT_Fan_1'
bulb2 = 'AIoT_Bulb_1'

# status
detect = '물체가 감지됨'
non_detect = '감지되지 않음'

# Database
iot_dht_sql = """insert into iot_space_dhtsensor values (%s, %s, %s, %s, %s)"""
iot_ir_sql = """insert into iot_space_irsensor values (%s, %s, %s, %s)"""
iot_fan_sql = """insert into iot_space_fan values (%s, %s, %s)"""
iot_bulb_sql = """insert into iot_space_bulb values (%s, %s, %s)"""
aiot_dht_sql = """insert into aiot_space_dhtsensor values (%s, %s, %s, %s, %s)"""
aiot_ir_sql = """insert into aiot_space_irsensor values (%s, %s, %s, %s)"""
aiot_fan_sql = """insert into aiot_space_fan values (%s, %s, %s)"""
aiot_bulb_sql = """insert into aiot_space_bulb values (%s, %s, %s)"""