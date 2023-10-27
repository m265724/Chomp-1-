import pygame
import sys
from work_chomp_utils import make_background, make_splash_screen, fish

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
pygame.display.set_caption('Chomp Game')

# Make static background.
background = scr.copy()
make_background(background)

# Create beginning screen
make_splash_screen(background, scr)

# Create fish
charles = fish(scr, 'green')
ted = fish(scr, 'orange')
ted.fish_x_speed = 0.2
marg = fish(scr, 'puffer')
marg.fish_x_speed = 0.3

# Run the game
running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position
    charles.update_position(scr)
    ted.update_position(scr)
    marg.update_position(scr)

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()