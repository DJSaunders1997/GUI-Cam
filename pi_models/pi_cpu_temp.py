# https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/

import os

def getCpuTemp():
    # Read data from Raspberry Pi (specifically read GPU temperature)
    temp = os.popen("vcgencmd measure_temp").read()
    
    return temp