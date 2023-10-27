from pgzhelper import *

class Ship(Actor):
    def __init__(self, x, y):
        super(Ship, self).__init__("ship")
        self.pos = (x, y)
        self.turning = 0 #otočenie
        self.accelerate = 0

    def update(self, w, h):
        self.angle = self.angle + self.turning

        if self.accelerate == 1:
            self.move_forward(2)

        if self.accelerate == -1:
            self.move_forward(-2)

        self.x = self.x % w
        self.y = self.y % h