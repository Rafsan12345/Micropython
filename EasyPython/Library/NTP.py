try:
	a = ''
	b = ''


	def begin(a,b):
		import ntptime
		import network
		#import time
		from machine import RTC #
		import time #sleep
		timeout =0 
		wifi = network.WLAN(network.STA_IF)

		# Restarting WiFi
		wifi.active(False)
		time.sleep(0.5)
		wifi.active(True)
		
		wifi.connect(a,b)
		
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



		#(2000, 1, 1, 0, 40, 8, 5, 1)
			
		
	def operate(utf):
		utf = int(utf)
		from machine import RTC #
		import time #sleep
		import ntptime
		import network
		from machine import RTC 
		rtc = RTC()
		ntptime.settime()
		UTC_OFFSET = +utf * 60 * 60 #>>for bd +6
		actual_time = time.localtime(time.time() + UTC_OFFSET)
		c = actual_time
		return c 

except:
	pass
		
