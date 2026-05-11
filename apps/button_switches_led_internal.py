# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Switch on a Kookaberry internal LED when a Kookaberry button is pressed

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka)
# |
# +─ REPEAT FOREVER
#       |
#       +─ IF Kookaberry BUTTON is_pressed -> SWITCH ON Kookaberry LED
#           + ELSE SWITCH OFF Kookaberry LED

# START of script

# IMPORT libraries (kooka)
import kooka

# REPEAT FOREVER
while True:

    # IF Kookaberry BUTTON is_pressed -> SWITCH ON Kookaberry LED
    if kooka.button_a.is_pressed():
        kooka.led_red.on()

    # ELSE SWITCH OFF Kookaberry LED
    else:
        kooka.led_red.off()

# END of script