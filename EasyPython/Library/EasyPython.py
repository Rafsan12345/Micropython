#

class RTC():
	from machine import RTC
	rtc = RTC()
	rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # set a specific date and time
	
try:

	def add(a,b):
		return a+b

	def sub(a,b):
		return a-b


	def blynk(pin,time_on,time_off):
		from machine import Pin
		import time
		p0 = Pin(pin,Pin.OUT)
		p0.on()
		time.sleep(time_on)
		p0.off()
		time.sleep(time_off)

	def digitalWrite(pin,Logic):
			from machine import Pin
			p0 = Pin(pin,Pin.OUT)
			p0.value(Logic)

	def digitalRead(pin):
		from machine import Pin
		p0 = Pin(pin,Pin.IN)
		return p0.value()

	def delay(ms):
		import time
		time.sleep(ms/1000)

	def analogRead():
		from machine import ADC
		adc = ADC(0) # create ADC object on ADC pin
		v = adc.read() # read value, 0-1024
		return v
	# unc
	def analogWrite(pin,value):
		from machine import Pin, PWM
		value = int(map(value,0,255,0,1023))
		pwm2 = PWM(Pin(pin), freq=500, duty=value)

	#unc
		
	#test
	def looping(a,b,c,d,e,m,n,time):
		from machine import Pin
		import time
		for i in range(m,n):
			listt = [a,b,c,d,e] #pin number
			cc = listt[i]
			Pin(cc,Pin.OUT).on()
			time.sleep(int(time/1000))
			Pin(cc,Pin.OUT).off()

	def lcd(message):
		import machine
		from machine import Pin,I2C
		from lcd_api import LcdApi
		from i2c_lcd import I2cLcd
		from time import sleep
		I2C_ADDR = 0x27
		totalRows = 2
		totalColumns = 16
		i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
		lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
		lcd.putstr(f"{message}")

	def clear():
		import machine
		from machine import Pin,I2C
		from lcd_api import LcdApi
		from i2c_lcd import I2cLcd
		from time import sleep
		I2C_ADDR = 0x27
		totalRows = 2
		totalColumns = 16
		i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266
		lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
		lcd.clear()


	def map(x,min1,max1,min2,max2):
		x = constrain(x,min1,max1)
		try:
			c = (x/max1)*max2
			return c
		except:
			c = 0



	def constrain(x,mi,mx):
		if x < mi :
			return mi
		elif x > mx:
			return mx
		else :
			return x
	#formate
	#c = f
	#f = decreasing(c)



	def increasing(c,step):
		c = c + step
		return c

	def decreasing(c,step):
		c = c - step
		return c

	def Serial_write(x):
		from machine import UART
		uart = UART(0, baudrate=115200) 
		uart.write(f'{x}\n')




	

except:
	pass





