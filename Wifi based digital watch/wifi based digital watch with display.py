import ntptime
import network
#import time
from machine import RTC #
timeout = 0
#
import machine
from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time #sleep




I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
#
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)

















wifi = network.WLAN(network.STA_IF)

# Restarting WiFi
wifi.active(False)
time.sleep(0.5)
wifi.active(True)

wifi.connect('HaVe A ReLaX 🥴🥵','10203040')

if not wifi.isconnected():
    print('connecting..')
    while (not wifi.isconnected() and timeout < 5):
        print(5 - timeout)
        timeout = timeout + 1
        time.sleep(1)
        
if(wifi.isconnected()):
    print('Connected')
else:
    print('Time Out')

c = 0 
fg = 0
ff = 0
h = 0
m = 0
s = 0

#(2000, 1, 1, 0, 40, 8, 5, 1)
    
    
lcd.putstr(" Digital Watch ")
while True:
	try:
		#
		
		import ntptime
		import network
		from machine import RTC 
		
		rtc = RTC()
		ntptime.settime()
		UTC_OFFSET = +6 * 60 * 60 #>>for bd +6
		actual_time = time.localtime(time.time() + UTC_OFFSET)
		c = actual_time
		
		
		
		fg = c[3]
		
		x = c[4]
		s = c[5]
		
		d = c[2]
		m = c[1]
		y = c[0]
		if fg > 12:
			fg = fg - 12
			lcd.putstr(f'Time>>{fg}:{x}PM')
			lcd.putstr("    ")
			lcd.putstr(f' Date>>{d}:{m}:{22}')
			time.sleep(1)
			lcd.clear()
			#print(c)
			
		else:
			lcd.putstr(f'Time>>{fg}:{x}AM')
			lcd.putstr("    ")
			lcd.putstr(f' Date>>{d}:{m}:{22}')
			time.sleep(1)
			lcd.clear()
		
		
		
		
		
		
		
	except:
		lcd.clear()
		lcd.putstr("Please Wait..")
		time.sleep(5)
		continue 
