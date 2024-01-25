import smbus2
import bme280
import time
from rpi_lcd import LCD
from gpiozero import Button
button = Button(20)

counter = 0
#instantiate
lcd = LCD()
address = 0x77

#bus address 4 is used for our sensor
bus = smbus2.SMBus(4)
calibration_params = bme280.load_calibration_params(bus, address)

running = True


while running == True:
        try:
                data = bme280.sample(bus,address,calibration_params)
                rounded_temp = round(data.temperature, 2)
                rounded_hum = round(data.humidity, 2)
                rounded_pres = round(data.pressure, 2)
                options =[rounded_temp, rounded_hum, rounded_pres]
                if counter == 0:
                    lcd.text(str(options[counter]), 1)
                    button.wait_for_press()
                    counter += 1
                elif counter == 1:
                    lcd.text(str(options[counter]), 1)
                    button.wait_for_press()
                    counter += 1
                elif counter == 2:
                    lcd.text(str(options[counter]), 1)
                    button.wait_for_press()
                    counter = 0
        except KeyboardInterrupt:
                running = False

#These variables could easily be written to a CSV file to allow for the recording of the data and possibly machine learning tasks
