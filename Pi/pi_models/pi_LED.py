#Module should encapsulate LED logic, and be used to turn LEDs On and Off.
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(23, GPIO.OUT)  # Green LED connected to pin 23 and shared GND
GPIO.setup(24, GPIO.OUT)  # Red LED connected to pin 24 and shared GND


def LED_on(led_pin_num):
    if (led_pin_num==23):
        print('Green LED on!')
        GPIO.output(23, GPIO.HIGH)
    elif (led_pin_num == 24):
        print('Red LED on!')
        GPIO.output(24,GPIO.HIGH)

def LED_off(led_pin_num):
    if (led_pin_num == 23):
        print('Green LED off!')
        GPIO.output(23,GPIO.LOW)
    elif (led_pin_num == 24):
        print('Red LED off!')
        GPIO.output(24,GPIO.LOW)

def change_led_state(led_pin_num):

    if (GPIO.input(led_pin_num)==0):    # returns 1 if pin state is HIGH 
        LED_on(led_pin_num)
    else:
        LED_off(led_pin_num)
