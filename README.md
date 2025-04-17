MicroPython Codes for OLED Displays (Raspberry Pi Pico)

Wiring:

GND → GND

VCC → 3V3

SCL → GP1

SDA → GP0

Files Included:
1. SH1106.py
(P.S. If you're using SSD1306 code and the display looks messed up, try this instead. I had the same issue.)

2. OLED_text.py
Displays your text on the screen. If you write a longer message and only part of it shows up, it's because the Raspberry Pi Pico doesn't automatically scale text.
To fix this, add another line right below:

          oled.text("Hello world,", 0, 0)  
          oled.text("Goodbye world,", 0, 15)

   By default, the OLED can show only 16 characters per line.

4. OLED_animation.py
Just a simple screensaver animation: a rectangle bouncing off the walls.

WARNINGS:

1.Make sure your display is I2C, otherwise, it probably won’t work.

2.If your display isn't 128x64 pixels, update the resolution in all your scripts. Example:
  oled = sh1106.SH1106_I2C(128, 64, i2c)

3.If your display isn’t responding, or throws errors like:
  OSError: [Errno 110] ETIMEDOUT
  ...that means it's not communicating with the microcontroller. Double-check your wiring.

4.If your display is I2C, the resolution is correct, all pins are correctly connected (GND, VCC, SCL, SDA), and it still doesn’t respond, then it's probably defective.
  You should request a refund. Most stores accept returns within 30 days as long as you have the receipt and the display is in its original condition, but always check the store’s policy first.

Enjoy!

Proudly made by

Thomas Vanek
