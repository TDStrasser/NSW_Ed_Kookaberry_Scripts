# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Blinking a LED on the Kookaberry 3 times using a for loop

# The Kookaberry has three in-built LEDs to use: kooka.led_red; kooka.led_orange; kooka.led_green
# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, sleep)
# +─ INITIALISE variables (blink_time)
# |
# +─ REPEAT 3 times
#       |
#       +─ SWITCH ON red / orange / green LED
#       +─ DELAY for blink_time
#       +─ SWITCH OFF red / orange / green LED
#       +─ DELAY for blink_time

# START the script

# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor
from time import sleep # import a library for time delays

# INITIALISE variables
blink_time = 0.5 # Sets the variable that determines the blink on/off time

# REPEAT 3 times
for count in range(3):  # Loop repeats 3 times (count = 0 -> 1 -> 2 -> loop exits on 3)
    # SWITCH ON LED
    kooka.led_green.on()
    
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time variable initialsed earlier
    
    # SWITCH OFF LED
    kooka.led_green.off()
    
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time variable initialsed earlier

    # END LOOP
    
# END of script