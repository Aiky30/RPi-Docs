import os
import time
from datetime import datetime

def get_cpu_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()
    
    # Convert the temp read from the OS to a clean float
    return float(cpu_temp.replace("temp=","").replace("'C\n", ""))

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # 24-Hour:Minute:Second
    return  current_time
                        
while True:    
    temperature = get_cpu_temp()
    bar_size = int(temperature) - 30
    bar = str("|" * bar_size) 
    
    print("{time} {temp} {graph}".format(
        time=get_time(), temp=temperature, graph=bar
    ))
    
    time.sleep(0.5)
        
