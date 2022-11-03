#from EasyPython2 import *
class lcdbegin():
	import machine
	from machine import Pin,I2C
	from lcd_api import LcdApi
	from i2c_lcd import I2cLcd
	I2C_ADDR = 0x27
	totalRows = 2
	totalColumns = 16
	i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       
	lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

