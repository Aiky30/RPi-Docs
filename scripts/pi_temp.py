import os
import time
from datetime import datetime

x_axis = []
y_axis = []
graph = []

def get_cpu_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    #Convert the temp read from the OS to a clean float
    return float(cpu_temp.replace("temp=","").replace("'C\n", ""))

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # 24-Hour:Minute:Second
    return  current_time
                        
while True:
    #Only keep the latest 5 inputs
    if len(x_axis) == 5 and len(y_axis) == 5:
        #Ignore the room temp
        multiplier = int(y_axis[0]) - 30
        print("|" * multiplier)
        del x_axis[0]
        del y_axis[0]
    else:
        print("Getting data...")
    #Add latest date
    x_axis.append(get_time())
    y_axis.append(get_cpu_temp())
    time.sleep(0.5)
        
