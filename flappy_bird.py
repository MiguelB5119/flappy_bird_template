# <Miguel Beira>
# start modules
import pgzrun

# create constants
WIDTH = 800
HEIGHT = 600

# print welcome
print('The game is about to start!')
print('Click the mouse to "flap" upwards')
print("Dodge the pipes and the floor")
print("Good luck and have fun!")

# make background
background = Actor('bg')
background.x = 400
background.y = 300

# make bird
bird = Actor('bird')
bird.x = 160
bird.y = 300

# make pipes


# draw everything to screen
def draw():
    screen.fill((128, 0, 0))

    # draw background
    background.draw()

    # draw characters
    bird.draw()

# update everything
def update():

    # update bird
    bird.y = bird.y + 1

    # update pipes


    # bird hits bottom of screen


    # bird hits pipes


# moving


# runs everything
pgzrun.go()