# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Detects a digital input Pin and correspondingly switches a LED connected to a Pin on the Kookaberry

# References:
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#class-display-access-to-the-kookaberry-s-oled-display-and-underlying-framebuffer

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Pin, sleep, Kookaberry display)
# +─ INITIALISE variables (delay_time)
# +─ INITIALISE Pin as an output for LED, second Pin as a digital input (e.g. for an infrared proximity sensor)
# +- INITIALISE Kookaberry display
# |
# +─ REPEAT FOREVER
#       |
#       +- CLEAR the Kookaberry display
#       +─ IF input Pin is ON THEN -> SWITCH LED ON -> PRINT "Object Detected"
#       |   + ELSE -> SWITCH LED OFF -> PRINT "Clear"
#       |
#       +- UPDATE Kookaberry display
#       +─ DELAY for delay_time

# START of script

# IMPORT libraries
from machine import Pin  # import the library for input/output Pins on the Kookaberry
from time import sleep # import a library for time delays
import kooka # import the library for the Kookaberry

# INITIALISE variables
delay_time = 0.1 # Sets the variable that determines how often the input is read

# INITIALISE Pins
led_output = Pin("P1", Pin.OUT) # Sets the Pin on plug P1 as an output
sensor_input = Pin("P2", Pin.IN) # Sets the Pin on plug P2 as an input

# INITIALISE Kookaberry display
display = kooka.display

# REPEAT forever
while True:
    # CLEAR the Kookaberry display
    display.clear()
    
    # IF input Pin is ON THEN -> SWITCH LED ON
    if sensor_input.value() == True:
        led_output.on()
        display.print("Object detected")
    # ELSE -> SWITCH LED OFF
    else:
        led_output.off()
        display.print("Clear")
    
    # UPDATE Kookaberry display
    display.show()
    
    # DELAY for blink_time
    sleep(delay_time) # Uses the delay time variable initialsed earlier


# END of script

