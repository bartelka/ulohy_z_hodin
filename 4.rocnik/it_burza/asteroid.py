from pgzhelper import *
import random

class Asteroid(Actor):
    def __init__(self, x, y):
        super(Asteroid, self).__init__("asteroid1")
        self.pos = (x, y)
        self.angle = random.randrange(360)

    def update(self,w,h):
        self.move_forward(2)

        self.x = self.x % w
        self.y = self.y % h