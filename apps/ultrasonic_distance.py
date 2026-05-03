# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring distance using an ultrasonic distance sensor connected to two Pins on the Kookaberry
# IMPORTANT: Use only the 3.3 volt distance sensors to avoid damaging the Kookaberry
#            e.g. Type RCWL1601 - https://core-electronics.com.au/33v-ultrasonic-distance-sensor.html

# Reference: Ultrasonic TBA pending

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Ultrasonic)
# |
# +─ INITIALISE Ultrasonic distance sensor
# |
# +─ READ the distance from the Ultrasonic sensor
# +- PRINT the distance on the REPL console
# |
# END

# START of script

# IMPORT libraries
from kooka.ultrasonic import Ultrasonic  # import the library for the Ultrasonic sensor on the Kookaberry

# INITIALISE Ultrasonic distance sensor
ultrasonic = Ultrasonic(trigger_pin="P3A", echo_pin="P3B") # The sensor is connected to Plug 3 on the Kookaberry

# READ the distance from the Ultrasonic sensor
distance = ultrasonic.distance()

# PRINT the distance on the REPL console
print("Distance is ", distance, "mm")

# END of script
