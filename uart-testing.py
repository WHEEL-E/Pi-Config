import serial

port = serial.Serial("/dev/ttyS0", 115200)
action = "a"
port.write(action.encode())
