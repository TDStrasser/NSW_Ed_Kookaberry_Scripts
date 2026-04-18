# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation
#
# Blinking a LED on the Kookaberry
# The Kookaberry has three in-built LEDs to use: kooka.led_red; kooka.led_orange; kooka.led_green
# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html
#
# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, sleep)
# +─ INITIALISE variables (blink_time)
# |
# +─ REPEAT FOREVER
#       |
#       +─ DELAY for blink_time
#       +─ TOGGLE red / orange / green LED (TOGGLE means switch on if off / off if on)
#
# The script begins here
# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor
from time import sleep # import a library for time delays
# INITIALISE variables
blink_time = 0.5 # Sets the variable that determines the blink on/off time
# REPEAT forever
while True:
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time variable initialsed earlier
    # TOGGLE the red / orange / green LED
    kooka.led_green.toggle() # Choices are led_red / led_orange / led_green
# End of script