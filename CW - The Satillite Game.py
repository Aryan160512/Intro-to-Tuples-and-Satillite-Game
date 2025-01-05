import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 584
TITLE = 'The Satillite Game'

satillites = []
nextSatillites = 0
numOfSatillites = 10

startTime = 0
totalTime = 0

lines = []

for i in range(numOfSatillites):
    satillite = Actor('satillite')
    satillite.pos = (random.randint(50, 750), random.randint(50, 534))
    satillites.append(satillite)

startTime = time()

def on_mouse_down(pos):
    global lines, nextSatillites

    if nextSatillites < numOfSatillites:
        if satillites[nextSatillites].collidepoint(pos):
            if nextSatillites:
                lines.append((satillites[nextSatillites - 1].pos, satillites[nextSatillites].pos))
            
            nextSatillites += 1
        
        else:
            lines.clear()
            nextSatillites = 0

def draw():
    global satillites, totalTime
    screen.clear()
    screen.blit('spacebg', (0, 0))

    number = 1

    for actor in satillites:
        actor.draw()
        screen.draw.text(f'{number}', (actor.pos[0] - 20, actor.pos[1] + 20))
        number += 1

    for l in lines:
        screen.draw.line(l[0], l[1], (255, 255, 255))

    if nextSatillites < numOfSatillites:
        totalTime = time() - startTime
        screen.draw.text(f'Time taken: {round(totalTime, 1)} seconds', (50, 50))
    else:
        screen.draw.text(f'Time taken to complete connections: {round(totalTime, 1)} seconds', (50, 50))
pgzrun.go()