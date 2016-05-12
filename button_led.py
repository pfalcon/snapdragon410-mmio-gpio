import utime as time
from apq8016_gpio import Pin

led1 = Pin(21)
switch3 = Pin(107)

# Light LED when on-board button S3 is pressed
while 1:
    # Inverted input
    led1.value(not switch3.value())
    # Don't burn CPU
    time.sleep(0.01)
