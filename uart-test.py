import serial


def main(action):
    port = serial.Serial(
        port="/dev/ttyS0",
        baudrate=115200,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        write_timeout=1,
    )
    port.write(action.encode())


main("a")
main("b")
main("c")
main("d")
