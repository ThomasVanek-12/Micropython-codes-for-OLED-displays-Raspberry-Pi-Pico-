from machine import Pin, I2C
import time
import sh1106

i2c = I2C(0, scl=Pin(1), sda=Pin(0), freq=400000)

oled = sh1106.SH1106_I2C(128, 64, i2c)

oled.fill(0)

oled.text("HELLO WORLD!", 0, 0)
oled.text("GOODBYE WORLD!", 0, 15)
oled.show()

while True:
    time.sleep(1)
