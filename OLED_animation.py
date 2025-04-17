from machine import Pin, I2C
import sh1106
import framebuf
import time

i2c = I2C(0, scl=Pin(1), sda=Pin(0))
oled = sh1106.SH1106_I2C(128, 64, i2c)

WIDTH = 128
HEIGHT = 64
buffer = bytearray(WIDTH * HEIGHT // 8)
fb = framebuf.FrameBuffer(buffer, WIDTH, HEIGHT, framebuf.MONO_VLSB)

w = 20
h = 10

x = 30
y = 20
dx = 1
dy = 1

while True:
    fb.fill(0)
    fb.fill_rect(x, y, w, h, 1)
    oled.framebuf.blit(fb, 0, 0)
    oled.show()
    x += dx
    y += dy
    if x <= 0 or x + w >= WIDTH:
        dx = -dx
    if y <= 0 or y + h >= HEIGHT:
        dy = -dy
    time.sleep(0.0001)
