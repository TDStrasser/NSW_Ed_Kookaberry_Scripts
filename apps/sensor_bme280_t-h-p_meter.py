# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring atmospheric temperature, humidity and air pressure using the BME280 sensor connected to two Pins (Plug P3) on the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/bme280.html#module-bme280

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, bme280, softI2C, fonts)
# |
# +─ INITIALISE BME280 lux sensor and I2C communications with it
# +- INITIALISE the Kookaberry OLED display
# +- INITIALISE the temperature, humidity, and air-pressure variables
# |
# +- EVERY 5 seconds
#     +─ READ temperature, humidity and air pressure from the BME280 sensor and format for printing
#     +- PRINT the the readings on the REPL console
#     +- PRINT the readings on the OLED display

# START of script

# IMPORT libraries (kooka, bme280, softI2C, fonts)
import kooka, fonts
from kooka.bme280 import BME280
from machine import SoftI2C

# INITIALISE BME280 sensor and I2C communications with it
i2c = SoftI2C(scl="P3A", sda="P3B")
bme280 = BME280(i2c, address=0x77)

# INITIALISE the Kookaberry OLED display
oled = kooka.display
oled.setfont(fonts.mono6x7) # Set font size to be smaller than default 8x8

# INITIALISE the BME280 sensor variables
temperature = None
humidity = None
air_pressure = None

# Main loop code.
while True:
    # EVERY 5 seconds.
    if kooka.time_passed(5):

        # READ the BME280 sensor data and format as character strings for printing
        temperature = "Temperature: {:.2f}C".format(bme280.temperature())
        humidity = "Humidity: {:.2f}%".format(bme280.humidity())
        air_pressure = "Pressure: {:.0f}hPa".format(bme280.pressure())

        # PRINT the readings on the REPL console
        print(temperature)
        print(humidity)
        print(air_pressure)

        # PRINT the readings on the OLED display
        oled.clear()
        oled.print("BME280 Readings", show=0)
        oled.print(temperature, show=0)
        oled.print(humidity, show=0)
        oled.print(air_pressure, show=0)
        oled.show()

# END of script