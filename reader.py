import smbus2
import bme280
import time
from rpi_lcd import LCD

#instantiate
lcd = LCD()

#Specify address of sensor
address = 0x77

#bus address 4 is used for our sensor
bus = smbus2.SMBus(4)
calibration_params = bme280.load_calibration_params(bus, address)

running = True


while running == True:
        try:
                data = bme280.sample(bus,address2,calibration_params)
                print(data.timestamp)
                print(data.temperature)
                print(data.pressure)
                print(data.humidity)

                rounded_temp = round(data.temperature, 2)
                rounded_hum = round(data.humidity, 2)
                rounded_pres = round(data.pressure, 2)
                lcd.text("Tem: " + str(rounded_temp) + "Hum: " + str(rounded_hum) + "% " + "Kpa " + str(rounded_pres), 1)
                time.sleep(3)
        except KeyboardInterrupt:
                running = False

#These variables could easily be written to a csv file to allow for recording of the data and possibly machine learning tasks
