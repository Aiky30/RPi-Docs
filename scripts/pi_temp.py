import os
import time


def get_cpu_temp():
        cpu_temp = os.popen("vcgencmd measure_temp").readline()
        return cpu_temp.replace("temp=","")


while True:
        print(get_cpu_temp())
        time.sleep(.5)
