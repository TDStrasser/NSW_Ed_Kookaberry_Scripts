# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring light level in lux using the VEML7700 sensor connected to two Pins (Plug P3) on the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/veml7700.html#module-veml7700

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, veml7700, softI2C)
# |
# +─ INITIALISE VEML7700 lux sensor and I2C communications with it
# +- INITIALISE the Kookaberry OLED display
# +- INITIALISE the lux_reading variable
# |
# +- EVERY 5 seconds
#     +─ READ the lux level from the VEML7700 sensor
#     +- PRINT the the lux level on the REPL console
#     +- PRINT the lux level on the OLED display

# START of script

# IMPORT libraries (kooka, veml7700, softI2C)
import kooka
from kooka.veml7700 import VEML7700
from machine import SoftI2C

# INITIALISE VEML7700 lux sensor and I2C communications with it
i2c = SoftI2C(scl="P3A", sda="P3B")
veml = VEML7700(i2c, address=0x10)

# INITIALISE the Kookaberry OLED display
oled = kooka.display

# INITIALISE the lux_reading variable
lux_reading = None

# Main loop code.
while True:
    # EVERY 5 seconds.
    if kooka.time_passed(5):
        # READ the lux level from the VEML7700 sensor
        lux_reading = veml.lux()

        # PRINT the the lux level on the REPL console
        print("Lux:", lux_reading)

        # PRINT the lux level on the OLED display
        oled.clear()
        oled.print('Lux:', lux_reading, show=0)
        oled.show()

# END of script