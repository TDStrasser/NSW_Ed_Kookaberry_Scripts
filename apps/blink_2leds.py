# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation
#
# Blinking two alternately LEDs on the Kookaberry
# The Kookaberry has three in-built LEDs to use: kooka.led_red; kooka.led_orange; kooka.led_green
#
# Description of the algorithm to be implemented
#START
# |
# +─ IMPORT libraries (kooka, sleep)
# +─ INITIALISE variables (blink_time)
# +- INITIALISE the first LED (turn it on)
# |
# +─ REPEAT FOREVER
#       |
#       +─ DELAY for blink_time
#       +─ TOGGLE first LED (TOGGLE means switch it on if off / off if on)
#       +─ TOGGLE second LED (TOGGLE means switch it on if off / off if on)
#
# The script begins here
# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor
from time import sleep # import a library for time delays
# INITIALISE variables
blink_time = 0.5 # Sets a variable with the blink on/off time; use it later
# INITIALISE the first LED by turning it on
kooka.led_red.on() # Turn the first LED on so it will turn off when first toggled
# REPEAT forever
while True:
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time initialised earlier
    # TOGGLE the red LED
    kooka.led_red.toggle() # Choices are led_red / led_orange / led_green
    # TOGGLE the red LED
    kooka.led_green.toggle() # Choices are led_red / led_orange / led_green
# End of script
