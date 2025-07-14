import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from digitalio import DigitalInOut, Direction, Pull
import neopixel

print("hello world")

NUM_PIXELS = 66        
USED_PIXELS = 66       
PIXEL_PIN = board.GP0 
BRIGHTNESS = 0.1

pixels = neopixel.NeoPixel(
    PIXEL_PIN, NUM_PIXELS, brightness=BRIGHTNESS, auto_write=False
)


COLORS = [(0, 0, 255), (255, 255, 0), (255, 0, 0)]

lightButton = {
    1: [16, (255, 0, 0)],
    2: [32, (255, 255, 0)],
    3: [48, (0, 0, 255)],
    4: [65, (255, 255, 255)]
}

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

button1 = setup_button(board.GP1)
button2 = setup_button(board.GP5)
button3 = setup_button(board.GP28)
button4 = setup_button(board.GP9)
enter = setup_cherry(board.GP22)
escape = setup_cherry(board.GP27)

prev_states = {
    button1: False,
    button2: False,
    button3: False,
    button4: False
}

button_keys = {
    button1: Keycode.W,
    button2: Keycode.A,
    button3: Keycode.S,
    button4: Keycode.D
}

button_nums = {
    button1: 1,
    button2: 2,
    button3: 3,
    button4: 4
}

def lightSection(buttonNum):
    color = lightButton[buttonNum][1]
    upper = lightButton[buttonNum][0]
    if buttonNum == 1:
        lower = 0
    else:
        lower = lightButton[buttonNum - 1][0]
    
    for index in range(0, NUM_PIXELS):
        if not ((index < upper) and (index > lower)):
            pixels[index] = (0,0,0)
        else:
            pixels[index] = color
    pixels.show()       
    

while True:
#     lightSection(1)
#     for i in range(0, 65):
#         print(i)
#         pixels[i] = (255,255,255)
        
    pixels.show()
    if not enter.value:
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)  # basic debounce

    if not escape.value:
        kbd.send(Keycode.ESCAPE)
        time.sleep(0.2)
# 
    for btn, prev in prev_states.items():
        current = btn.value

        if prev and not current:
            kbd.send(button_keys[btn]) 
            lightSection(button_nums[btn])
        elif not prev and current:  # just released
            kbd.press(button_keys[btn])
            lightSection(button_nums[btn])
        prev_states[btn] = current
    time.sleep(0.01)