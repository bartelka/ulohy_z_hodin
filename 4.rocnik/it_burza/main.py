import pgzrun
import random

from ship import Ship
from asteroid import Asteroid

#rozmery platna
WIDTH = 900
HEIGHT = 500

perfect_ship = Ship(WIDTH/2, HEIGHT/2) #inštancia
asteroid1 = Asteroid(random.randrange(WIDTH), random.randrange(HEIGHT))

def on_key_down(key):
    if key == keys.RIGHT:
        perfect_ship.turning = -5
    if key == keys.LEFT:
        perfect_ship.turning = 5
    if key == keys.UP:
        perfect_ship.accelerate = 1
    if key == keys.DOWN:
        perfect_ship.accelerate = -1

def on_key_up(key):
    if key == keys.RIGHT:
        perfect_ship.turning = 0
    if key == keys.LEFT:
        perfect_ship.turning = 0
    if key == keys.UP:
        perfect_ship.accelerate = 0
    if key == keys.DOWN:
        perfect_ship.accelerate = 0

#funkcia potrebna na vykreslenie lode
def draw():
    screen.clear()
    perfect_ship.draw()
    asteroid1.draw()

def update():
    perfect_ship.update(WIDTH,HEIGHT)
    asteroid1.update(WIDTH,HEIGHT)

pgzrun.go()