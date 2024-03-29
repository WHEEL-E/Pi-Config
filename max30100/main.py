import time
import max30100

mx30 = max30100.MAX30100()
mx30.set_led_current(led_current_red=30.6, led_current_ir=30.6)
mx30.enable_spo2()

while True:
    mx30.read_sensor()

    mx30.ir, mx30.red

    hb = int(mx30.ir / 100)
    spo2 = int(mx30.red / 100)

    if mx30.ir != mx30.buffer_ir:
        print("Pulse:", hb)
    if mx30.red != mx30.buffer_red:
        print("SPO2:", spo2)

    time.sleep(1)
