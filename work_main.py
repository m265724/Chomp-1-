import pygame
import sys
from work_chomp_utils import make_background, make_splash_screen, Fish, C_Fish
import time

# Initialize Pygame
pygame.init()

# Create pygame clock
clock = pygame.time.Clock()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning main.py.')
print('-------------------------------------------\n')

# Specify screen dimensions.
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen.
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Chomp Game')

# Make static background.
background = scr.copy()
make_background(background)

# Create beginning screen
#make_splash_screen(background, scr)

# Create fish
num_fish = 2
fish_list = []
for i in range(0, int(num_fish/2)):
    fish_list.append(Fish(scr, "green"))
for i in range(0, int(num_fish/2)):
    fish_list.append(Fish(scr, "orange"))
mary = C_Fish(scr, 'puffer')

# Run the game
running = True
while running:

    t1 = time.time()

    # Stores events in a variable
    events = pygame.event.get()

    # Get events happening in window.
    for event in events:

        # User presses quit button
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position
    for fish in fish_list:
        fish.update_position(scr)
    mary.update_position(scr, events)

    # Check for collision
    mary.collision_check(fish_list)

    # Update the display
    pygame.display.flip()

    # Make fish move at 60fps
    clock.tick(60)

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()
