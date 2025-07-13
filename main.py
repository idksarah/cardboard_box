#This tutorial is provided by TomoDesign / https://www.instagram.com/tomo_designs/ 
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

print("hello world")

kbd = Keyboard(usb_hid.devices)

# define buttons. these can be any physical switches/buttons, but the values
button1 = digitalio.DigitalInOut(board.GP1)
button1.direction = digitalio.Direction.INPUT
button1.pull = digitalio.Pull.UP

button2 = digitalio.DigitalInOut(board.GP2)
button2.direction = digitalio.Direction.INPUT
button2.pull = digitalio.Pull.UP

button15 = digitalio.DigitalInOut(board.GP15)
button15.direction = digitalio.Direction.INPUT
button15.pull = digitalio.Pull.UP

button16 = digitalio.DigitalInOut(board.GP16)
button16.direction = digitalio.Direction.INPUT
button16.pull = digitalio.Pull.UP

while True:
    if button1.value:
        kbd.send(Keycode.W)
    if button2.value:
        kbd.send(Keycode.D)
    if button15.value:
        kbd.send(Keycode.A)
    if button16.value:
        kbd.send(Keycode.S)

    time.sleep(0.08)