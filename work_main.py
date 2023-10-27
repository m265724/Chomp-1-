import pygame
import sys
from work_chomp_utils import make_background, make_splash_screen
import random

class fish:
    def __init__ (self, screen, color):
        # Create a single fish
        fish_name = f'assests/sprites/{color}_fish.png'
        self.fish_img = pygame.image.load(fish_name).convert()
        self.fish_img.set_colorkey((0,0,0)) # makes area around fish transparent
        self.fish_x = random.randint(0,screen.get_width() - self.fish_img.get_width())
        self.fish_x_dir = 1
        self.fish_x_speed = 0.2
        self.fish_y = random.randint(0,screen.get_width() - 4*self.fish_img.get_height())
        self.fish_y_dir = 1
        self.fish_y_speed = 0.2

    def update_position(self, screen):
        # Load images
        sand = pygame.image.load("assets/sprites/sand.png").convert()
        sand_top = pygame.image.load("assets/sprites/sand_top.png").convert()

        # Update fish's positions
        self.fish_x += self.fish_x_speed*self.fish_x_dir
        self.fish_y += self.fish_y_speed*self.fish_y_dir

        # Move fish on screen
        if self.fish_x >= screen.get_width() - self.fish_img.get_width():
            self.fish_x_dir = -1
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)

        if self.fish_x < 0:
            self.fish_x_dir = 1
            self.fish_img = pygame.transform.flip(self.fish_img, True, False)

        if self.fish_y < 0:
            self.fish_y_dir = 1

        if self.fish_y >= screen.get_height() - self.fish_img.get_height() - sand.get_height() - sand_top.get_height():
            self.fish_y_dir = -1

        # Draw fish
        screen.blit(self.fish_img, (self.fish_x,self.fish_y))

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
# make_splash_screen(background, scr)

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