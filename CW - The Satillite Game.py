import pgzrun
import random

WIDTH = 1000
HEIGHT = 600
TITLE = 'The Satillite Game'

satillites = []
nextSatillites = 0
numOfSatillites = 10

for i in range(numOfSatillites):
    satillite = Actor('satillite')
    satillite.pos = (random.randint(50, 950), random.randint(50, 550))
    satillites.append(satillite)

def draw():
    global satillites
    screen.clear()
    screen.blit('spacebg', (0, 0))

    number = 1

    for actor in satillites:
        actor.draw()
        screen.draw.text(f'{number}', (actor.pos[0] - 30, actor.pos[1] + 30))
        number += 1
pgzrun.go()