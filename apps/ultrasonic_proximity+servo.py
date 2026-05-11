# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring proximity using an ultrasonic distance sensor connected to Pins on the Kookaberry (Plug P3)
# Operates a Servo (connected to Plug P1) when proximity changes
# Lights an external LED (connected to Plug P2) when the Servo is activated while proximity remains on
# IMPORTANT: Use only the 3.3 volt distance sensors to avoid damaging the Kookaberry
#            e.g. Type RCWL1601 - https://core-electronics.com.au/33v-ultrasonic-distance-sensor.html

# Reference: Ultrasonic TBA pending
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#kooka.kooka.Servo

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (Ultrasonic, Pin, Servo, sleep)
# |
# +─ INITIALISE proximity threshold distance variable (proximate)
# +─ INITIALISE Ultrasonic distance sensor
# +─ INITIALISE Pin attached to LED as OUTPUT
# +- INITIALISE Servo
# |
# +─ REPEAT FOREVER
#       |
#       +─ READ the distance from the Ultrasonic sensor
#       |
#       +─ IF distance <= proximate threshold THEN -> SWITCH LED ON -> SET Servo to OPEN position -> WAIT for 5 seconds
#           + ELSE -> SWITCH LED OFF -> SET Servo to CLOSED position

# START of script

# IMPORT libraries
from kooka.ultrasonic import Ultrasonic  # import the library for the Ultrasonic sensor on the Kookaberry
from machine import Pin  # import the library for input/output Pins on the Kookaberry
from kooka import Servo
from time import sleep

# INITIALISE proximity distance variable (proximate)
proximate = 25 # Distance in mm below which proximity is detected

# INITIALISE Ultrasonic distance sensor
ultrasonic = Ultrasonic(trigger_pin="P3A", echo_pin="P3B") # The sensor is connected to Plug 3 on the Kookaberry

# INITIALISE Pin as output
led_output = Pin("P1", Pin.OUT) # Sets the Pin on plug P1 as an output

# INITIALISE Servo
servo = Servo("P2") # Define a servo connected to Kookaberry plug P2

# REPEAT forever
while True:
    # READ the distance from the Ultrasonic sensor
    distance = ultrasonic.distance()
    
    # IF distance <= proximate threshold THEN -> SWITCH LED ON -> SET Servo to OPEN position -> WAIT for 5 seconds
    if distance <= proximate:
        led_output.on() 
        servo.angle(90)
        sleep(5)

    # ELSE -> SWITCH LED OFF -> SET Servo to CLOSED position
    else:
        led_output.off()
        servo.angle(0)

# END of script
