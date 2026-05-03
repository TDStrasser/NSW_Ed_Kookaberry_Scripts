# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring proximity using an ultrasonic distance sensor and a LED connected to Pins on the Kookaberry
# IMPORTANT: Use only the 3.3 volt distance sensors to avoid damaging the Kookaberry
#            e.g. Type RCWL1601 - https://core-electronics.com.au/33v-ultrasonic-distance-sensor.html

# Reference: Ultrasonic TBA pending
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Ultrasonic, Pin)
# |
# +─ INITIALISE proximity threshold distance variable (proximate)
# +─ INITIALISE Ultrasonic distance sensor
# +─ INITIALISE Pin attached to LED as OUTPUT
# |
# +─ REPEAT FOREVER
#       |
#       +─ READ the distance from the Ultrasonic sensor
#       |
#       +─ IF distance <= proximate threshold THEN -> SWITCH LED ON
#           + ELSE -> SWITCH LED OFF

# START of script

# IMPORT libraries
from kooka.ultrasonic import Ultrasonic  # import the library for the Ultrasonic sensor on the Kookaberry
from machine import Pin  # import the library for input/output Pins on the Kookaberry

# INITIALISE proximity distance variable (proximate)
proximate = 25 # Distance in mm below which proximity is detected

# INITIALISE Ultrasonic distance sensor
ultrasonic = Ultrasonic(trigger_pin="P3A", echo_pin="P3B") # The sensor is connected to Plug 3 on the Kookaberry

# INITIALISE Pin as output
led_output = Pin("P1", Pin.OUT) # Sets the Pin on plug P1 as an output

# REPEAT forever
while True:
    # READ the distance from the Ultrasonic sensor
    distance = ultrasonic.distance()
    
    # IF distance <= proximate threshold THEN -> SWITCH LED ON
    if distance <= proximate:
        led_output.on()
    # ELSE -> SWITCH LED OFF
    else:
        led_output.off()

# END of script
