# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Moving a servo at a set speed using the Kookaberry
# IMPORTANT: Use a continuous type of Servo with this script

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#kooka.kooka.Servo

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka)
# |
# +─ INITIALISE variable (speed) in range -100 to +100 - the actual speed depends on the mechanics of the Servo
# |
# +- INITIALISE Servo 
# |
# +- SET Servo to the preset speed
# END

# START of script

# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor

# INITIALISE variable (speed)
speed = 50 # Sets the value of the desired speed.

# INITIALISE Servo
servo = kooka.Servo('P1') # Define a servo connected to Kookaberry plug P1

# SET Servo speed to the preset value
servo.speed(speed) # Set the Servo to the predefined speed

# END of script
