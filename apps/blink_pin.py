# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Blinking a LED connected to a Pin on the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Pin, sleep)
# +─ INITIALISE variables (blink_time)
# +─ INITIALISE Pin as an output
# |
# +─ REPEAT FOREVER
#       |
#       +─ DELAY for blink_time
#       +─ TOGGLE Pin output to control an external LED (TOGGLE means switch on if off / off if on)

# START of script

# IMPORT libraries
from machine import Pin  # import the library for input/output Pins on the Kookaberry
from time import sleep # import a library for time delays

# INITIALISE variables
blink_time = 0.5 # Sets the variable that determines the blink on/off time

# INITIALISE Pin as output
led_output = Pin("P1", Pin.OUT) # Sets the Pin on plug P1 as an output

# REPEAT forever
while True:
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time variable initialsed earlier

    # TOGGLE the red / orange / green LED
    led_output.toggle()

# END of script
