# Text beginning with # is a comment
# This MicroPython script for the Kookaberry was prepared by the AustSTEM Foundation

# Measuring atmospheric temperature and humidity using the DHT22 sensor connected to Plug P1 on the Kookaberry

# Reference: https://kookaberry-reference-guide.readthedocs.io/en/latest/dht.html#module-dht 

# Description of the algorithm to be implemented
# START
# |
# +─ IMPORT libraries (kooka, dht22, fonts, time)
# |
# +─ INITIALISE DHT22 sensor
# +- INITIALISE the Kookaberry OLED display
# +- INITIALISE the temperature and humidity variables
# |
# +- EVERY 5 seconds
#     +─ READ temperature and humidity from the DHT22 sensor and format for printing
#     +- PRINT the the readings on the REPL console
#     +- PRINT the readings on the OLED display

# START of script

# IMPORT libraries (kooka, dht22, fonts)
import kooka, fonts
from kooka.dht import DHT22
from time import sleep

# INITIALISE DHT22 sensor on Plug P1
dht = DHT22("P1")

# INITIALISE the Kookaberry OLED display
oled = kooka.display
oled.setfont(fonts.mono6x7) # Set font size to be smaller than default 8x8

# INITIALISE the BME280 sensor variables
temperature = None
humidity = None

# Main loop code.
while True:
    # EVERY 5 seconds.
    if kooka.time_passed(5):

        # READ the DHT22 sensor data and format as character strings for printing
        temperature = "Temperature: {:.2f}C".format(dht.temperature())
        sleep(2) # DHT sensors require 1-2 seconds between readings
        humidity = "Humidity: {:.2f}%".format(dht.humidity())

        # PRINT the the lux level on the REPL console
        print(temperature)
        print(humidity)

        # PRINT the readings on the OLED display
        oled.clear()
        oled.print("DHT22 Readings", show=0)
        oled.print(temperature, show=0)
        oled.print(humidity, show=0)
        oled.show()

# END of script