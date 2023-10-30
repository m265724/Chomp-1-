import pygame
import sys
from work_chomp_utils import make_background, make_splash_screen, fish, C_Fish

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
make_splash_screen(background, scr)

# Create fish
charles = fish(scr, 'green')
ted = fish(scr, 'orange')
mary = C_Fish(scr, 'puffer')

# Run the game
running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():

        # Does something when a key is pressed
        # *insert code*

        # User presses quit button
        if event.type == pygame.QUIT:
            running = False

    # Draw background.
    scr.blit(background, (0, 0))

    # Update fish position
    charles.update_position(scr)
    ted.update_position(scr)
    mary.update_position(scr)

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