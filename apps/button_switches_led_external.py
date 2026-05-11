# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Switch on an external LED when an external button is pressed.

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka)
# +- INITIALISE Button and LED
# |
# +─ REPEAT FOREVER
#       |
#       +─ IF BUTTON is_pressed -> SWITCH ON LED
#           + ELSE SWITCH OFF LED

# START of script

# IMPORT libraries (kooka)
import kooka

# INITIALISE Button and LED (button connected to Pin P2, LED to P1)
button = kooka.Button("P2")
led = kooka.LED("P1")

# REPEAT FOREVER
while True:

    # IF BUTTON is_pressed -> SWITCH ON LED
    if button.is_pressed():
        led.on()

    # ELSE SWITCH OFF LED
    else:
        led.off()

# END of script