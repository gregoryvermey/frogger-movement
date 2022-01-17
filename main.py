# Programmer: Mr. Devet
# Date: 2021-12-06
# Description: 

# Import and initialize the pygame library
import pygame
from pygame.locals import *
pygame.init()

from pygame_grid import *
from sprite import *
from sys import exit

# Create and open a pygame screen with the given size
screen = pygame.display.set_mode((612, 394))
grid = make_grid()

# Set the title of the pygame screen
pygame.display.set_caption("Fishies")

# Create a clock to keep track of time
clock = pygame.time.Clock()

# Group to hold all of the active sprites
all_sprites = pygame.sprite.Group()

### SET UP YOUR GAME HERE

# Load the images
background = pygame.image.load("underwater.jpg")
screen.blit(background, (0,0))

fish_image = pygame.image.load("fish.png")
fish_image = pygame.transform.flip(fish_image, True, False)
fish_image = pygame.transform.rotozoom(fish_image, 0, 0.5)

squid_image = pygame.image.load("squid.png")
squid_image = pygame.transform.rotozoom(squid_image, 0, 0.35)

# Group that holds just the squids
squids = pygame.sprite.Group()

# Create the sprites
fish = Sprite(fish_image)
fish.center = (306,197)
fish.add(all_sprites)

squid1 = Sprite(squid_image)
squid1.position = (50,50)
squid1.speed = 2
squid1.direction = 270
squid1.rotates = False
squid1.add(all_sprites, squids)

squid2 = Sprite(squid_image)
squid2.position = (450,50)
squid2.speed = 3
squid2.direction = 180
squid2.rotates = False
squid2.add(all_sprites, squids)

squid3 = Sprite(squid_image)
squid3.position=(50,250)
squid3.speed = 1
squid3.rotates = False
squid3.add(all_sprites, squids)

squid4 = Sprite(squid_image)
squid4.position=(450,250)
squid4.speed = 4
squid4.direction = 135
squid4.rotates = False
squid4.add(all_sprites, squids)

# Set the keys to repeat when held for 100 milliseconds
pygame.key.set_repeat(30)

# Variable for the number of lives
lives = 3

# Main Loop
while True:
    # Set the frame rate to 30 frames per second
    time = clock.tick(30)

    ### MANAGE IN-GAME EVENTS HERE

    # Loop through all of the events
    for event in pygame.event.get():
        # If the user hits the close button, exit
        if event.type == QUIT:
            exit()

        # Move the fish when the arrow keys are pressed
        elif event.type == KEYDOWN:
            # Move forward on up arrow key
            if event.key == K_UP:
                fish.move_forward(3)

            # Move backward on down arrow key
            elif event.key == K_DOWN:
                fish.move_backward(3)

            # Turn left on left arrow key
            elif event.key == K_LEFT:
                fish.turn_left(5)

            # Turn right on right arrow key
            elif event.key == K_RIGHT:
                fish.turn_right(5)

    # Check if the fish is touching a squid
    for squid in squids:
        if pygame.sprite.collide_mask(fish, squid):
            # Move the fish to the starting location
            fish.center = (306,197)
            # Lose a life
            lives -= 1
            if lives == 0:
                exit()

    # Draw the background on the screen
    screen.blit(background, (0,0))

    # Update the sprites' locations
    all_sprites.update()

    # Check if squid is off screen and if so, bounce it
    for squid in squids:
        if squid.left < 0 or squid.right > 612:
            squid.direction = 180 - squid.direction
        if squid.top < 0 or squid.bottom > 394:
            squid.direction = 360 - squid.direction

    # Draw the sprites on the screen
    all_sprites.draw(screen)

    # Uncomment the next line to show a grid
    #screen.blit(grid, (0,0))

    # Flip the changes to the screen to the computer display
    pygame.display.flip()