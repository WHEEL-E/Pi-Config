from time import sleep

import serial


def main(action):
    port = serial.Serial(
        "/dev/ttyS0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
    )
    port.write(action.encode())


while True:
    main("a")
    sleep(1)
    main("b")
    sleep(1)
