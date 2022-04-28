"""
For more information on the serial module, see: https://pythonhosted.org/pyserial/index.html
"""

import serial
import time

port = serial.Serial(
    port="/dev/ttyS0",
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    write_timeout=1,
)

def A():
    port.write(b"A")

def B():
    port.write(b"B")

A()
time.sleep(2)
B()