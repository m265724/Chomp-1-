import pygame
import sys
from chomp_utils import make_background

# Initialize Pygame
pygame.init()

# Clear terminal output.
for ii in range(0, 10):
    print()

print('\nRunning make_background.py.')
print('-------------------------------------------\n')

# Screen dimensions
scr_wid = 800  # (px)
scr_hgt = 600  # (px)

# Create the screen
scr = pygame.display.set_mode((scr_wid, scr_hgt))
pygame.display.set_caption('Making a customized background')

background = scr.copy()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




#Load images
water = pygame.image.load("assests/sprites/water.png").convert()
reg_sand = pygame.image.load("assests/sprites/sand.png").convert()
top_sand = pygame.image.load("assests/sprites/sand_top.png").convert()

img_px = 64

#Draw image on screen
    #draw water
for x in range(0,scr_wid,img_px):
    for y in range(0,scr_hgt,img_px):
        scr.blit(water,(x,y))

    #draw sand
for xx in range(0,scr_wid,img_px):
    for yy in range(550,scr_hgt,img_px):
        scr.blit(reg_sand,(xx,yy))

    #draw top sand
for xxx in range(0,scr_wid,img_px):
    for yyy in range(500,550,img_px):
        scr.blit(top_sand, (xxx,yyy))

running = True
while running:

    # Get events happening in window.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the display
    pygame.display.flip()

# End of game loop.
print('\n-------------------------------------------')
print('End of line.')

# Quit Pygame
pygame.quit()
sys.exit()