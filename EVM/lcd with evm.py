from machine import UART,Pin
import time
from machine import Timer
import machine
from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
##

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16


i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)       #initializing the I2C method for ESP8266

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColumns)
##

#lcd.putstr("1234567")
#sleep(2)
#lcd.clear()



##

p0 = Pin(2,Pin.OUT) #output pin define
#input
p1 = Pin(0, Pin.IN, Pin.PULL_UP)  #input pin define
p2 = Pin(14, Pin.IN, Pin.PULL_UP)
p3 = Pin(12, Pin.IN, Pin.PULL_UP)
p4 = Pin(13, Pin.IN, Pin.PULL_UP)
#input

a = 0
b = 0
c = 0
d = 0
a1= 0
b1= 0
c1 = 0
aaa = 0

bbb = 0

ccc = 0
v = 0
ddd =  0
p0.off() # bulb indecator system ok


ax = 1
bx = 1
cx = 1
av = 1
bv = 1
cv = 1
print("pressed your vote\n[A]  [B]  [C]")
lcd.putstr("Welcome to EVM\n")
sleep(5)
lcd.clear()
lcd.putstr("Press your vote\n")
lcd.putstr(" [A][B][C][SET]")
while True:
    #try:
       #...............................................!
	aa = p1.value()
	bb = p2.value()
	cc = p3.value()
	dd = p4.value()
	
	
	if (aa == 0 and aaa == 0 and bx==1 and cx ==1 and av == 1 ): 
		a = a + 1
		a1 = a
		aaa = 1
		print('You pressed [A]\n')
		lcd.clear()
		lcd.putstr("You pressed [A]")
		time.sleep(0.5)
		
	elif (aa == 1 and aaa == 1 ):
		aaa = 0
		av = 0
		ax = 0
		
		
		
	elif (bb == 0 and bbb == 0 and ax ==1 and cx == 1 and bv == 1 ): # c = limit of increasing <'11'
		b = b + 1
		b1 = b
		bbb = 1
		print('You pressed [B]\n')
		lcd.clear()
		lcd.putstr("You pressed [B]")
		time.sleep(0.5)
		
	elif (bb == 1 and bbb == 1 ):
		bbb = 0
		bx = 0
		bv = 0
		
		
	elif (cc == 0 and ccc == 0 and ax ==1 and bx ==1 and cv ==1): # c = limit of increasing <'11'
		c = c + 1
		c1 = c
		ccc = 1
		print('You pressed [C]\n')
		lcd.clear()
		lcd.putstr("You pressed [C]")
		time.sleep(0.5)
		
	elif (cc == 1 and ccc == 1 ):
		ccc = 0
		cx = 0
		cv = 0
		
	elif (dd == 0  ):
		nid = open('nid.txt','r')
		vote = open('vote.txt','a')
		chek = open('chek.txt','r') #changable
		n = nid.read()
		ch = chek.read()
		lcd.clear()
		lcd.putstr("input your NID")
		x = input("input your NID:::-")
		
		
		
		if x in n and x not in ch :
			vote.write(f'A{a1} B{b1} C{c1}\n')
			chek = open('chek.txt','a')
			chek.write(f"{x}\n")
			vote.close()
			nid.close()
			chek.close()
			ax = 1
			bx = 1
			cx = 1
			
			av = 1
			bv = 1
			cv = 1
			lcd.clear()
			
			lcd.putstr("Your vote Sucessfully Completed")
			print('Your vote Sucessfully Completed....')
			print('\n')
			print('\n')
			print("pressed your vote\n[A]  [B]  [C]")
			lcd.clear()
			lcd.putstr("Press your vote\n")
			lcd.putstr("[A][B][C][SET]")
		else:
			ax = 1
			bx = 1
			cx = 1
			
			av = 1
			bv = 1
			cv = 1
			lcd.clear()
			lcd.putstr("NID miscmatch")
			sleep(1)
			lcd.clear()
			lcd.putstr("Your vote is    alrady Collect..")
			print("Dont match you NID\n")
			print("or\nYour vote is alrady Collect\n")
			print("pressed your vote\n[A]  [B]  [C]")
			sleep(1)
			lcd.clear()
			lcd.putstr("Press your vote\n")
			lcd.putstr(" [A][B][C][SET]")
			continue 
		
		
		
		
		
		
		
	else:
		pass

        
        
        
        
       #................................................!
'''  except:
        print("problem detect")
        p0.on() # bulb off system is crashed
        break
'''
    


