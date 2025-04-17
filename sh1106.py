from micropython import const
import utime as time
import framebuf

# Příkazy pro SH1106
_SET_CONTRAST = const(0x81)
_SET_NORM_INV = const(0xA6)
_SET_DISP = const(0xAE)
_SET_SCAN_DIR = const(0xC0)
_SET_SEG_REMAP = const(0xA0)
_LOW_COLUMN_ADDRESS = const(0x00)
_HIGH_COLUMN_ADDRESS = const(0x10)
_SET_PAGE_ADDRESS = const(0xB0)

class SH1106_I2C:
    def __init__(self, width, height, i2c, addr=0x3C, rotate=0):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.pages = self.height // 8
        self.buffer = bytearray(self.width * self.pages)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def write_data(self, buf):
        self.i2c.writeto(self.addr, bytearray([0x40]) + buf)

    def init_display(self):
        for cmd in (
            _SET_DISP | 0x00,  # Display off
            0x20, 0x00,        # Set Memory Addressing Mode
            _SET_CONTRAST, 0x80,
            _SET_SEG_REMAP | 0x01,
            _SET_SCAN_DIR | 0x08,
            _SET_DISP | 0x01   # Display on
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def fill(self, color):
        self.framebuf.fill(color)

    def text(self, text, x, y, color=1):
        self.framebuf.text(text, x, y, color)

    def show(self):
        for page in range(self.pages):
            self.write_cmd(_SET_PAGE_ADDRESS | page)
            self.write_cmd(_LOW_COLUMN_ADDRESS | 2)
            self.write_cmd(_HIGH_COLUMN_ADDRESS | 0)
            start = self.width * page
            end = start + self.width
            self.write_data(self.buffer[start:end])
