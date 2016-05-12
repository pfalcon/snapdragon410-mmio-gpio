import utime as time
from apq8016_gpio import Pin

# Only 2 of 4 Dragonboard410c LEDs are on SoC GPIOs
led1 = Pin(21)
led2 = Pin(120)

leds = [led1, led2]

while 1:
    for led in leds:
        led.value(1)
        time.sleep(0.5)
        led.value(0)
