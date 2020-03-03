from sense_hat import SenseHat
from random import randint

sense = SenseHat()

randomcolortext = (randint(0, 255), randint(0, 255), randint(0, 255))
randomcolorback = (randint(0, 255), randint(0, 255), randint(0, 255))

while True: 
  sense.low_light = True
  sense.show_message("Hello! We are New Media Development :)",text_colour=randomcolortext,back_colour=randomcolorback)