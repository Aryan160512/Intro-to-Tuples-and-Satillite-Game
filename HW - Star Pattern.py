import pgzrun, random

WIDTH = 800
HEIGHT = 450
TITLE = 'Star Pattern Game'

stars = []
nextStars = 0
numOfStars = 10

for i in range(numOfStars):
    alien = Actor('star')
    alien.pos = (random.randint(50, 750), random.randint(50, 400))
    stars.append(alien)
    

def draw():
    global stars
    screen.clear()
    screen.blit('spacebg1', (0, 0))

    number = 1

    for actor in stars:
        actor.draw()
        screen.draw.text(f'{number}',( actor.pos[0] - 20, actor.pos[1] + 20))
        number += 1

pgzrun.go()