import pgzrun, random
from time import time

WIDTH = 800
HEIGHT = 450
TITLE = 'Star Pattern Game'

stars = []
nextStars = 0
numOfStars = 10

startTime = 0
totalTime = 0

lines = []

for i in range(numOfStars):
    alien = Actor('star')
    alien.pos = (random.randint(50, 750), random.randint(50, 400))
    stars.append(alien)
    
startTime = time()

def on_mouse_down(pos):
    global lines, nextStars

    if nextStars < numOfStars:
        if stars[nextStars].collidepoint(pos):
            if nextStars:
                lines.append((stars[nextStars - 1].pos, stars[nextStars].pos))
            
            nextStars += 1     
        
        else:
               lines.clear()
               nextStars = 0

def draw():
    global stars, totalTime
    screen.clear()
    screen.blit('spacebg1', (0, 0))

    number = 1

    for actor in stars:
        actor.draw()
        screen.draw.text(f'{number}',( actor.pos[0] - 20, actor.pos[1] + 20))
        number += 1

    for l in lines:
        screen.draw.line(l[0], l[1], (255, 255, 255))

    if nextStars < numOfStars:
        totalTime = time() - startTime
        screen.draw.text(f'Time taken: {round(totalTime, 1)} seconds', (50, 50))
    else:
        screen.draw.text(f'Time taken to complete connections: {round(totalTime, 1)} seconds', (50, 50))

pgzrun.go()