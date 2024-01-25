# Raspberry-pi-iot
This showcases my IOT skills using Python and Raspberry Pi with popular sensors



This is an IOT-enabled weather station capable of giving us an insight into the temperature, pressure, and humidity, we can view these stats on a UI
implemented on an LCD which can be cycled with the use of a button that toggles through each view.

Before we could begin our project we had to do the following to allow our Raspberry Pi 4 model B to use multiple i2c ports since both our devices require
this for communication with the PI

We first edited the boot file to include this line
dtoverlay=i2c-gpio,bus=5,i2c_gpio_sda=12,i2c_gpio_scl=13

Then we rebooted our Pi and used the corresponding GPIO pins as the SCA and SCL pins for our environmental sensor

we can then use the bus number we configured to search for our device and its address using 
sudo i2cdetect -y [bus_no]

This will be useful for addressing our devices in our program

All the libraries used apart from the RPI.bme280 were already available on the official Raspberry Pi image





