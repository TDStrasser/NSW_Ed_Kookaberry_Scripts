# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Format and show information on the Kookaberry's display

# The Kookaberry has three in-built LEDs to use: kooka.led_red; kooka.led_orange; kooka.led_green
# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/kooka.html#class-display-access-to-the-kookaberry-s-oled-display-and-underlying-framebuffer

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka)
# +─ INITIALISE variables (text, number)
# +- INITIALISE the Kookaberry display
# |
# +─ PLACE information on the Kookaberry display (literal string, string variable, number)
# +- UPDATE the Kookaberry display

# START the script

# IMPORT libraries
import kooka  # import the library for the Kookaberry microprocessor

# INITIALISE variables
myString = "Car spaces left" # Defines a variable containing a character string
myNumber = 4 # Defines a variable containg a number

# INITIALISE the Kookaberry display
display = kooka.display # Gives the display a name
display.clear() # Clears the display

# PLACE information on the Kookaberry display (literal string, string variable, number)
# Note: text placement co-ordinates are defined by the lower left corner of the text on the display
#       top-left co-ordinate is x=0, y=0, bottom-right is x=127, y=63
#       default character size is 8 x 8 pixels
display.text("Park & Ride", 0, 10, 1) # Place literal string at display coordinates x=0, y=10, colour=1
display.text(myString, 0, 20, 1)      # Place myString variable contents at display coordinates x=0, y=20, colour=1
display.text(str(myNumber), 0, 30, 1) # Place myNumber converted to a string at display coordinates x=0, y=30, colour=1

# UPDATE the Kookaberry display
display.show() # Transfers the formatted contents to the physical display

# END of script
