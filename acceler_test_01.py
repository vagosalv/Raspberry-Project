import time
from datetime import datetime
import board
import adafruit_adxl34x
import csv


i2c = board.I2C()
accelerometer = adafruit_adxl34x.ADXL343(i2c)
accelerometer.data_rate = adafruit_adxl34x.DataRate.RATE_200_HZ
print(accelerometer.data_rate)

header = ["Time", "X-axis", "Y-axis", "Z-axis"]

def processing_loop(csvfile):
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([header]) 
    while True:
        Data = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f ") + "%f %f %f" % accelerometer.acceleration
        print(Data) 
        csv_writer.writerow([Data])
        csvfile.flush()


with open("dedomena.csv", "w") as csvfile:
    processing_loop(csvfile)
