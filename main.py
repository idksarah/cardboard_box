import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull

print("hello world")

# led = DigitalInOut(board.GP3)
# led.direction = Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)

def setup_button(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn

def setup_cherry(pin):
    btn = digitalio.DigitalInOut(pin)
    btn.direction = digitalio.Direction.INPUT
    btn.pull = digitalio.Pull.UP
    return btn

button1 = setup_button(board.GP3)
button2 = setup_button(board.GP2)
button15 = setup_button(board.GP1)
button16 = setup_button(board.GP16)
enter = setup_cherry(board.GP7)
escape = setup_cherry(board.GP9)

# Button states: True means unpressed, False means pressed
prev_states = {
    button1: True,
    button2: True,
    button15: True,
    button16: True
}

button_keys = {
    button1: Keycode.D,
    button2: Keycode.S,
    button15: Keycode.W,
    button16: Keycode.A
}

while True:    
#     led.value = False
#     print (button1.vaaaaaalue)
    if not enter.value:
        kbd.send(Keycode.ENTER)
    if not escape.value:
        kbd.send(Keycode.ESCAPE)
    for btn, prev in prev_states.items():
        current = btn.value
        if prev and not current:  # just pressed
            kbd.release(button_keys[btn])
        elif not prev and current:  # just released
            kbd.press(button_keys[btn])
        prev_states[btn] = current
    time.sleep(0.01)