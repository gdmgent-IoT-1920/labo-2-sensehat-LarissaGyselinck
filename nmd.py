from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

randcolor1 = (randint(0, 255), randint(0, 255), randint(0, 255))
randcolor2 = (randint(0, 255), randint(0, 255), randint(0, 255))
randcolor3 = (randint(0, 255), randint(0, 255), randint(0, 255))

while True:
  sense.show_letter("N", randcolor1)
  sleep(1)
  sense.show_letter("M", randcolor2)
  sleep(1)
  sense.show_letter("D", randcolor3)
  sleep(3)