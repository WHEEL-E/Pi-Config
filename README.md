# Pi-config

## Steps to configure Pi

1. Copy ssh and wpa_supplicant files to the pi root directory
2. Power on the pi and use putty to connect to it
    * Set the Host Name field to `raspberrypi.local`
    * Port should be set to `22`
    * Connection type should be set to `SSH`
    * The default user name is: `pi`
    * The default password is: `raspberry`
3. Open raspberrypi configuration `sudo raspi-config`
4. Enable `VNC`, `Serial`, `Camera` and `Expand filesystem`
5. Complete the setup using `bash setup.txt`

## Run script at startup

`sudo nano /etc/rc.local`
