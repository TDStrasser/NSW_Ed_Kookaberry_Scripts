# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring temperature using the DS18x20 temperature probe connected to Plug P1 on the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/ds18x20.html 

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, ds18x20, fonts)
# |
# +─ INITIALISE DS18X20 sensor
# +- INITIALISE the Kookaberry OLED display
# +- INITIALISE the temperature variable
# |
# +- EVERY 5 seconds
#     +─ READ temperature from the DS18X20 sensor and format for printing
#     +- PRINT the the reading on the REPL console
#     +- PRINT the reading on the OLED display

# START of script

# IMPORT libraries (kooka, ds18x20, fonts)
import kooka, fonts
from kooka.ds18x20 import DS18X20

# INITIALISE DS18X20 sensor on Plug P1
ds18x20 = DS18X20("P1")

# INITIALISE the Kookaberry OLED display
oled = kooka.display
oled.setfont(fonts.mono6x7) # Set font size to be smaller than default 8x8

# INITIALISE the DHT22 sensor variables
temperature = None

# Main loop code.
while True:
    # EVERY 5 seconds.
    if kooka.time_passed(5):

        # READ the DS18X20 sensor data and format as a character string for printing
        temperature = "Temperature: {:.2f}C".format(ds18x20.temperature())

        # PRINT the reading on the REPL console
        print(temperature)

        # PRINT the reading on the OLED display
        oled.clear()
        oled.print("DS18X20 Reading", show=0)
        oled.print(temperature, show=0)
        oled.show()

# END of script