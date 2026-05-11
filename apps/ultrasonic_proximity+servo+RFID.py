# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring proximity using an ultrasonic distance sensor connected to Pins on the Kookaberry (Plug P3)
# Operates a Servo (connected to Plug P1) when a valid RFID tag to be presented to the tag reader (connected to Plug P6)
# Lights an external LED (connected to Plug P2) when the Servo is activated while proximity remains on
# IMPORTANT: Use only the 3.3 volt distance sensors to avoid damaging the Kookaberry
#            e.g. Type RCWL1601 - https://core-electronics.com.au/33v-ultrasonic-distance-sensor.html

# Reference: Ultrasonic TBA pending
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/machine.Pin.html#class-pin-control-i-o-pins
#  https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#kooka.kooka.Servo

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (RFID [PN532 or RC522], Ultrasonic, Pin, Servo, sleep)
# |
# +─ INITIALISE proximity threshold distance variable (proximate)
# +─ INITIALISE RFID reader
# +─ INITIALISE Ultrasonic distance sensor
# +─ INITIALISE Pin attached to LED as OUTPUT
# +- INITIALISE Servo
# |
# +─ REPEAT FOREVER
#       |
#       +─ READ the distance from the Ultrasonic sensor
#       |
#       +─ IF distance <= proximate threshold AND valid RFID tag THEN -> SWITCH LED ON -> SET Servo to OPEN position -> WAIT for 5 seconds
#           + ELSE IF distance > proximate threshold THEN -> SWITCH LED OFF -> SET Servo to CLOSED position

# START of script

# IMPORT libraries
from kooka.pn532 import PN532 as RFID # import the RFID reader library
# from kooka.rc522 import RC522 as RFID # alternative import the RFID reader library
from kooka.ultrasonic import Ultrasonic  # import the library for the Ultrasonic sensor on the Kookaberry
from machine import Pin, SoftI2C  # import the library for input/output Pins and I2C communications on the Kookaberry
from kooka import Servo
from time import sleep

# INITIALISE proximity distance variable (proximate)
proximate = 25 # Distance in mm below which proximity is detected

# INITIALISE RFID reader (on plug P6 contining Pins GP4 and GP5)
i2c = SoftI2C(scl="GP5", sda="GP4")
rfid = RFID(i2c, address=36)

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
    
    # IF distance <= proximate threshold AND valid RFID tag THEN -> SWITCH LED ON -> SET Servo to OPEN position -> WAIT for 5 seconds
    if distance <= proximate and rfid.tag_present():
        led_output.on() 
        servo.angle(90)
        sleep(5)

    # ELSE -> SWITCH LED OFF -> SET Servo to CLOSED position
    elif distance > proximate:
        led_output.off()
        servo.angle(0)

# END of script
