# https://www.e-tinkers.com/2018/04/how-to-control-raspberry-pi-gpio-via-http-web-server/

import os

def getCpuTemp():
    '''
    Reads temperature data from Raspberry Pi CPU
    '''
    # Read data from Raspberry Pi (specifically read GPU temperature)
    temp = os.popen("vcgencmd measure_temp").read()
    
    return temp[5:9]    # From "temp=55.8'C\n" to 55.8