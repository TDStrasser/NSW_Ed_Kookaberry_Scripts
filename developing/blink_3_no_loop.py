# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Blinking a LED 3 times on the Kookaberry

# The Kookaberry has three in-built LEDs to use: kooka.led_red; kooka.led_orange; kooka.led_green
# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, sleep)
# +─ INITIALISE variables (blink_time)
# |
# +- BLINK LED 1st: ON -> DELAY -> OFF -> DELAY
# +- BLINK LED 2nd: ON -> DELAY -> OFF -> DELAY
# +- BLINK LED 3rd: ON -> DELAY -> OFF -> DELAY

# START the script

# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor
from time import sleep # import a library for time delays

# INITIALISE variables
blink_time = 0.5 # Sets the variable that determines the blink on/off time

# +- BLINK LED 1st: ON -> DELAY -> OFF -> DELAY
kooka.led_green.on() # Choices are led_red / led_orange / led_green
sleep(blink_time) # Uses the blink time variable initialsed earlier
kooka.led_green.off()
sleep(blink_time)

# +- BLINK LED 2nd: ON -> DELAY -> OFF -> DELAY
kooka.led_green.on() # Choices are led_red / led_orange / led_green
sleep(blink_time) # Uses the blink time variable initialsed earlier
kooka.led_green.off()
sleep(blink_time)

# +- BLINK LED 3rd: ON -> DELAY -> OFF -> DELAY
kooka.led_green.on() # Choices are led_red / led_orange / led_green
sleep(blink_time) # Uses the blink time variable initialsed earlier
kooka.led_green.off()
sleep(blink_time)

# END of script
