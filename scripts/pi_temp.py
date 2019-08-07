import os
import time
from datetime import datetime

#Lists for graph
x_axis = []
y_axis = []

def get_cpu_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    #Convert the temp read from the OS to a clean float
    return float(cpu_temp.replace("temp=","").replace("'C\n", ""))

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # 24-Hour:Minute:Second
    return  current_time
                        
while True:
    #Add latest date
    x_axis.append(get_time())
    y_axis.append(get_cpu_temp())
    #Create elements for graph
    latest_time = str(x_axis[-1]) + " " 
    latest_temp = str(y_axis[-1]) + " "
    temp_lines = str("|" * (int(y_axis[-1]) - 30))
    #Print line for graph every .5 seconds
    print(latest_time + latest_temp + temp_lines)
    time.sleep(0.5)
        
