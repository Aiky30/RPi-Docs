import os
import time
from datetime import datetime
import logging


logging.basicConfig(
    filename = '/var/log/shed-pi.log',
    level = logging.INFO,
    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
)
logger = logging.getLogger("parent")
TIME_TO_SLEEP = 60 # time in seconds


def check_os():
    return os.uname()[4].startswith("arm") 

def get_cpu_temp():
    cpu_temp = os.popen("vcgencmd measure_temp").readline()

    # Convert the temp read from the OS to a clean float
    return float(cpu_temp.replace("temp=","").replace("'C\n", ""))

def get_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S") # 24-Hour:Minute:Second
    return current_time

def main():

    logger.info(f"Shed pi started: {get_time()}")

    if not check_os():
        logger.error("only rasbian os supported")
        return

    while True:
        temperature = get_cpu_temp()
        logger.info(f"Pi temp: {temperature}")

        time.sleep(TIME_TO_SLEEP)

if __name__ == "__main__":
    main()
