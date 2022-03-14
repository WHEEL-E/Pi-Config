import serial

port = serial.Serial("/dev/ttyS0", 9600)
action = "a"
port.write(action.encode())
