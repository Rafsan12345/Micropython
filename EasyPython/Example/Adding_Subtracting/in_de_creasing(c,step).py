from EasyPython import *
c = 0
f = 0
while True:
	#increasing(c,step) ++
	#decreasing(c,step) --
	# step>> per repetition value added x = x + step
	'''
	#using fromate:
	c = f
	f = decreasing(c)
	'''
	c = f 
	f = increasing(c,5) #step 5 > 5,10,15,20..............
	delay(500) #print after 0.5 seconds
	print(f)   #prinr value of f










