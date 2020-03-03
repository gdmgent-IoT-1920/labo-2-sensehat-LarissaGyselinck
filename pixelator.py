from sense_hat import SenseHat
from random import randint
from time import sleep

sense = SenseHat()

row = 0
column = 0

def randcolor():
	return (randint(0, 255), randint(0, 255), randint(0, 255))

while True:
	for row in range(8):
		for column in range(8):
			sleep(0.2)
			sense.set_pixel(row, column, randcolor())