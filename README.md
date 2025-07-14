# highway ddr fnf lvochild type shiiiiiiiiiiiiiiiiiiiiiit

A scrappy 6-button LED dance pad emulating a Dance Dance Revolution pad — can be used for rhythm games like **Friday Night Funkin'** and other 4-key movement games. Includes **Enter** and **Escape** keys on top of the standard WASD/Arrow layout.

![cardboard box](images/box.jpg)
![fairy](images/fairy.jpg)

Built for **Hack Club Undercity** because we thought it'd be fun and my friend won't stop playing FNF IDK TBH.

---

## BOM

| Item                    | Quantity | Notes                  |
|-------------------------|----------|------------------------|
| Orpheus Pico            | 1        | Microcontroller        |
| Buzzers (with switches) | 4        | Act as the buttons     |
| Jumper wires (M/F)      | —        | For wiring everything  |
| Cables                  | —        | Any usable wires       |
| USB-C Cable             | 1        | For power & flashing   |
| Trash Box               | 1        | Housing / case         |
| Solder                  | —        |                        |
| Soldering Iron          | 1        | Required to solder     |

---

## Firmware

- [CircuitPython for Orpheus Pico](https://circuitpython.org/board/orpheus_pico/)

---

## Usage

1. Plug in your Orpheus Pico  
2. Download CircuitPython from the [official site](https://circuitpython.org/board/orpheus_pico/)  
3. Bootload it (double-tap the reset button until the drive shows up)  
4. Once it mounts as a USB drive:
    - Drag the `lib` folder into the root  
    - Drop in your `main.py`  
5. Boom. You're running DDR on homemade hardware LMFAO
--
## the PROCESS
-we decapitated a button
![cardboard box](images/diassembled_button.jpg)
world's worst soldering job
![cardboard box](images/wiring.png)


