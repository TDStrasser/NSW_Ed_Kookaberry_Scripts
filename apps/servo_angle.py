# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Moving a servo to a set angle using the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#kooka.kooka.Servo

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka)
# |
# +─ INITIALISE variable (angle) in the range -90 to +90 degrees
# |
# +- INITIALISE Servo 
# |
# +- SET Servo position to the preset angle
# END

# START of script

# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor

# INITIALISE variable (angle)
angle = 45 # Sets the value of the angle to be set in degrees.

# INITIALISE Servo
servo = kooka.Servo('P1') # Define a servo connected to Kookaberry plug P1

# SET Servo position to the preset angle
servo.angle(angle) # Move the Servo to preset angle

# END of script
