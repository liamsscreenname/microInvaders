from microbit import *
import random

disp = Image("00000:" * 5)

#displays an "enemy" at a random position 0-4 on the top row of the display
#a new enemy is generated every (sleep time)
def newEnemy():
	for x in range (0,5):
		disp.set_pixel(x, 0, 0)
	disp.set_pixel(random.randint(0,4), 0, 9)

newEnemy()
enemyHit = False

while True:
	t = running_time()

	#measure how much device is tilted left or right
	tilt = int((accelerometer.get_x() + 1024)/512)

	#clear the bottom row
	for x in range (0,5):
		disp.set_pixel(x, 4, 0)

	#put pixel on bottom row according to tilt
	disp.set_pixel(tilt, 4, 9)

	if enemyHit:
		newEnemy()



	display.show(disp)
	sleep(200)