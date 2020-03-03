from sense_hat import SenseHat 
from time import sleep

sense = SenseHat()

white = (0, 0, 0)
dgreen = (40, 114, 51)
green = (0, 255, 0)
dorange = (214, 118, 30)
lorange = (255, 165, 0)
beige = (255, 198, 163)
lgreen = (144, 238, 144)
dred = (139, 0, 0)
red = (255, 0, 0)
lred = (255, 192, 203)
dpurple = (128, 0, 128)
lpurple = (150, 111, 214)

avatar_pumpkin = [
	white, white, white, dgreen, dgreen, white, white, white,
	white, dorange, dorange, dgreen, dgreen, lorange, lorange, lorange,
	dorange, dorange, dorange, green, green, lorange, lorange, lorange,
	dorange, dorange, dorange, lorange, lorange, lorange, beige, lorange,
	dorange, dorange, lorange, lorange, lorange, beige, beige, lorange,
	dorange, dorange, lorange, lorange, lorange, lorange, lorange, lorange,
	dorange, dorange, lorange, lorange, lorange, lorange, lorange, lorange,
	white, dorange, dorange, dorange, dorange, dorange, dorange, white
]

avatar_tomato = [
	white, white, white, dgreen, green, white, white, white,
	white, dred, dgreen, dgreen, lgreen, green, red, white,
	dred, dred, dgreen, green, green, green, red, red,
	dred, dred, dred, dgreen, green, red, lred, red,
	dred, red, red, red, red, red, red, lred, red,
	dred, dred, red, red, red, red, lred, red, red,
	dred, dred, red, red, red, red, red, red, red,
	white, dred, dred, dred, dred, dred, dred, white
]

avatar_eggplant = [
	white, white, white, dgreen, green, white, white, white,
	white, dpurple, dpurple, dgreen, green, dpurple, dpurple, white,
	dpurple, dpurple, dgreen, dgreen, green, green, dpurple, dpurple,
	dpurple, dpurple, dpurple, green, green, dpurple, dpurple, dpurple,
	dpurple, dpurple, dpurple, dpurple, dpurple, dpurple, lpurple, dpurple,
	dpurple, dpurple, dpurple, dpurple, lpurple, lpurple, dpurple, dpurple,
	dpurple, dpurple, dpurple, dpurple, dpurple, dpurple, dpurple, dpurple,
	white, dpurple, dpurple, dpurple, dpurple, dpurple, dpurple, white
]

avatar_carrots = [
	white, dgreen, green, green, white, green, white, dgreen,
	white, white, green, white, white, white, dgreen, white,
	white, lorange, dgreen, lorange, white, dorange, dgreen, lorange,
	white, lorange, lorange, lorange, white, dorange, lorange, lorange,
	white, dorange, dorange, lorange, white, dorange, lorange, lorange,
	white, dorange, dorange, lorange, white, dorange, lorange, lorange,
	white, white, dorange, white, white, white, lorange, white,
	white, white, white, white, white, white, white, white
]

avatars = [avatar_pumpkin, avatar_tomato, avatar_eggplant, avatar_carrots]

while True:
	for avatar in avatars:
		sense.set_pixels(avatar)
		sleep(0.3)

