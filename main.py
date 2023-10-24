import pygame
import sys
from chomp_utils import make_background, make_splash_screen
# import chomp_utils

# Initialize Pygame
pygame.init()

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
pygame.display.set_caption('Making a customized background')

# Make static background.
background = scr.copy()
make_background(background)

# Create splash screen
# make_splash_screen(background, scr)

# Create a single fish
fish_img = pygame.image.load('assests/sprites/green_fish.png').convert()
fish_img.set_colorkey((0,0,0)) # makes area around fish transparent
fish_x = 0
fish_x_dir = 1
fish_y = 0
fish_y_dir = 1

print('Running Game ----')


running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    #Update fish's positions
    fish_x += 0.1*fish_x_dir
    fish_y  = 0*fish_y_dir

    # Move fish on screen
    if fish_x >= scr.get_width() - fish_img.get_width():
        fish_x_dir = -1
        fish_img = pygame.transform.flip(fish_img, True, False)

    if fish_x < 0:
        fish_x_dir = 1
        fish_img = pygame.transform.flip(fish_img, True, False)

    # Draw fish
    scr.blit(fish_img, (fish_x,fish_y))

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()