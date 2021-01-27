from smbus import SMBus
from pynput import keyboard
import time
import RPi.GPIO as GPIO
import numpy as np

addr = 0x8 # bus address
bus = SMBus(1) # indicates /dev/ic2-1
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
#GPIO.setup(12,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
#servo2 = GPIO.PWM(12,50)
servo1.start(0)
#servo2.start(0)
servo1.ChangeDutyCycle(2+(180/18))
#servo2.ChangeDutyCycle(2+(90/18))
time.sleep(0.015)

def on_press(key):
    try:
        k = key.char
    except:
        k = 'p'
    try:
        if k in ['w','W','8']:
            bus.write_byte(addr, int(1)) # switch it on
            print('alphanumeric key {0} pressed'.format(
                key.char))
        elif k in ['s','S','5','2']:
            bus.write_byte(addr, int(3))
            print('alphanumeric key {0} pressed'.format(
                key.char))
        elif k in ['A','a','4']:
            bus.write_byte(addr, int(4))
            print('alphanumeric key {0} pressed'.format(
                key.char))
        elif k in ['d','D','6']:
            bus.write_byte(addr, int(5))
            print('alphanumeric key {0} pressed'.format(
                key.char))
        elif k in ['e','E','9']:
            servo1.ChangeDutyCycle(2+(180/18))
            #servo2.ChangeDutyCycle(2+(90/18))
            time.sleep(0.15)
            
        elif k in ['r','R','+']:
            servo1.ChangeDutyCycle(2+(90/18))
            #servo2.ChangeDutyCycle(2+(180/18))
            time.sleep(0.15)
        elif k in ['f', 'F','1']:
            f = open("check.txt","w")
            f.write("1")
            f.close
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
def on_release(key):
    print('{0} released'.format(
        key))
    bus.write_byte(addr, int(2))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()


print('quit successfully')
servo1.ChangeDutyCycle(2+(180/18))
#servo2.ChangeDutyCycle(2+(90/18))
time.sleep(0.015)
servo1.ChangeDutyCycle(0)
servo1.stop()
time.sleep(0.015)
#servo2.ChangeDutyCycle(0)
#servo2.stop()
time.sleep(0.015)
GPIO.cleanup()
