from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

r=(255,0,0)
p=(207,185,151)
blue=(0,0,255)
black=(0,0,0)

mario = [
  black, black, r, r, r, black, black, black,
  black, black, r, r, r, r, r, black,
  black, black, p, black, p, black, black, black,
  black, black, p, p, black, p, black, black,
  black, blue, blue, r, blue, r, black, black,
  blue, black, blue, p, r, p, blue, black,
  black, black, r, r, r, r, black, black,
  black, black, blue, black, black, blue, black, black
]

mario_jump = [
  black, black, p, black, p, black, black, black,
  black, black, p, p, black, p, black, black,
  black, blue, blue, r, blue, r, black, black,
  blue, black, blue, p, r, p, blue, black,
  black, black, r, r, r, r, black, black,
  black, black, blue, black, black, blue, black, black,
  black, black, black, black, black, black, black, black,
  black, black, black, black, black, black, black, black
]

sense.set_pixels(mario)

for event in sense.stick.get_events():
  sense.set_pixels(mario_jump)
  sleep(1)
  sense.set_pixels(mario)