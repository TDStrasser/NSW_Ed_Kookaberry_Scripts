# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation
#
# Moving a servo between three positions using the Kookaberry
# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#kooka.kooka.Servo
#
# Description of the algorithm to be implemented
#START
# |
# +─ IMPORT libraries (kooka, sleep)
# +─ INITIALISE variables (open_time, close_time)
# +- INITIALISE Servo and set its position to 0 degrees
# |
# +─ REPEAT FOREVER
#       |
#       +- MOVE Servo to 45 degrees
#       +─ DELAY
#       +- MOVE Servo to 90 degrees
#       +─ DELAY
#       +- MOVE Servo back to 0 degrees
#       +─ DELAY
#
# The script begins here
# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor
from time import sleep # import a library for time delays
# INITIALISE variables
delay_time = 1.5 # Sets the variable that determines the delay time in seconds. Defined once used many times below.
# INITIALISE Servo and set its position to 0 degrees
servo = kooka.Servo('P1') # Define a servo connected to Kookaberry plug P1
servo.angle(0) # Move the Servo to 0 degrees
# REPEAT forever
while True:
    # MOVE Servo to 45 degrees
    servo.angle(45) # Move the Servo to 0 degrees
    # DELAY for open_time
    sleep(delay_time) # Uses the open time variable initialsed earlier
    # MOVE Servo to 90 degrees
    servo.angle(90) # Move the Servo to 0 degrees
    # DELAY for open_time
    sleep(delay_time) # Uses the open time variable initialsed earlier
    # TOGGLE the red / orange / green LED
    servo.angle(0) # Move the Servo back to 0 degrees
    # DELAY for close_time
    sleep(delay_time) # Uses the close time variable initialsed earlier
# End of script

