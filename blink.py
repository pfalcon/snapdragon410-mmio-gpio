import utime as time
from apq8016_gpio import Pin

led1 = Pin(21)

while 1:
    led1.value(1)
    time.sleep(0.5)
    led1.value(0)
    time.sleep(0.5)
