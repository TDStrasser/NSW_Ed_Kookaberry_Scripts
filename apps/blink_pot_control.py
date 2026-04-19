# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Control the blinking rate of a LED connected to a Pin on the Kookaberry using a potentiometer on a second Pin

# References: https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins
#             https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.ADC.html

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Pin, ADC, sleep)
# +─ INITIALISE variables (blink_time_min, blink_time_max)
# +─ INITIALISE Pins: P1 as an output, P2 as an ADC (analogue to digital converter) input
# |
# +─ REPEAT FOREVER
#       |
#       +─ READ the analogue input and use it to set the blink_time
#       +─ DELAY for blink_time
#       +─ TOGGLE Pin output to control an external LED (TOGGLE means switch on if off / off if on)

# START of script

# IMPORT libraries
from machine import Pin  # import the library for input/output Pins on the Kookaberry
from machine import ADC  # import the library for converting analogue inputs to digital numbers
from time import sleep # import a library for time delays

# INITIALISE variables
blink_time_min = 0 # Sets the variable that determines the minimum blink on/off time
blink_time_max = 1.0 # Sets the variable that determines the maximum blink on/off time

# INITIALISE Pins as output
led_output = Pin("P1", Pin.OUT) # Sets the Pin on plug P1 as an output
potentiometer = ADC("P2") # Sets plug P2 as an analogue input

# REPEAT forever
while True:
    # READ the analogue input and use it to set the blink_time
    control_input = potentiometer.read_u16() / 65535 # Results in a number between 0 and 1 inclusive
    blink_time = control_input * (blink_time_max - blink_time_min) + blink_time_min # Scale input to fit between the minimum and maximum blink times
    
    # DELAY for blink_time
    sleep(blink_time) # Uses the blink time variable initialsed earlier
    
    # TOGGLE the red / orange / green LED
    led_output.toggle()

# END of script

