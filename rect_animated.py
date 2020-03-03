from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

g = (0, 255, 255)
b = (255, 255, 255)

rect1 = [
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, g, g, b, b, b,
	b, b, b, g, g, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b
]

rect2 = [
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b,
	b, b, g, g, g, g, b, b,
	b, b, g, b, b, g, b, b,
	b, b, g, b, b, g, b, b,
	b, b, g, g, g, g, b, b,
	b, b, b, b, b, b, b, b,
	b, b, b, b, b, b, b, b
]

rect3 = [
	b, b, b, b, b, b, b, b,
	b, g, g, g, g, g, g, b,
	b, g, b, b, b, b, g, b,
	b, g, b, b, b, b, g, b,
	b, g, b, b, b, b, g, b,
	b, g, b, b, b, b, g, b,
	b, g, g, g, g, g, g, b,
	b, b, b, b, b, b, b, b
]

rect4 = [
	g, g, g, g, g, g, g, g,
	g, b, b, b, b, b, b, g,
	g, b, b, b, b, b, b, g,
	g, b, b, b, b, b, b, g,
	g, b, b, b, b, b, b, g,
	g, b, b, b, b, b, b, g,
	g, b, b, b, b, b, b, g,
	g, g, g, g, g, g, g, g
]

while True:
	sense.set_pixels(rect1)
	sleep(0.3)
	sense.set_pixels(rect2)
	sleep(0.3)
	sense.set_pixels(rect3)
	sleep(0.3)
	sense.set_pixels(rect4)
	sleep(0.3)
	sense.set_pixels(rect3)
	sleep(0.3)
	sense.set_pixels(rect2)
	sleep(0.3)
	sense.set_pixels(rect1)