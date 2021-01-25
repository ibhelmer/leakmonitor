import csv
import time
from w1thermsensor import W1ThermSensor

with open('measurement.csv', 'w', newline='') as file:
    start = time.time()
    writer = csv.writer(file)
    writer.writerow(["Timestamp","Sensor1","Sensor2","Diff"])
    for i in range(10000):
        mess = []
        for sensor in W1ThermSensor.get_available_sensors():
            mess.append(sensor.get_temperature())
        writer.writerow([str(round(time.time()-start,2)),str(mess[0]) ,str(mess[1]), str(mess[0]-mess[1])])
        time.sleep(8.2)		# 10 sec - measurement time
        print(i)		# Print mesurement count
