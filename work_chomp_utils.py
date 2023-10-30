import pygame
import random
import time

def make_background(surface):
    # Load the images.
    water = pygame.image.load("assets/sprites/water.png").convert()
    sand = pygame.image.load("assets/sprites/sand.png").convert()
    sand_top = pygame.image.load("assets/sprites/sand_top.png").convert()
    seagrass = pygame.image.load("assets/sprites/seagrass.png").convert()

    # Makes black pixels transparent.
    sand_top.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    # Cover screen with water.
    for x in range(0, surface.get_width(), water.get_width()):
        for y in range(0, surface.get_height(), water.get_height()):
            surface.blit(water, (x, y))

    # Draw base sand at bottom of screen.
    for x in range(0, surface.get_width(), sand.get_width()):
        surface.blit(sand, (x, surface.get_height() - sand.get_height()))

    # Draw top sand (has divots) on top of base sand.
    for x in range(0, surface.get_width(), sand_top.get_width()):
        surface.blit(sand_top, (x, surface.get_height() - sand.get_height() - sand_top.get_height()))

    # Draw seagrass.
    for _ in range(0, 15):
        x = random.randint(0, surface.get_width() - seagrass.get_width())
        surface.blit(seagrass, (x, surface.get_height() - sand.get_height() - sand_top.get_height()
                                - seagrass.get_height() + 5))

def make_splash_screen(background,scr):
    custom_font = pygame.font.Font('assests/fonts/Black_Crayon.ttf', 128)
    text = custom_font.render('Chomp',False,(255,69,0))
    scr.blit(background, (0,0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 50))
    pygame.display.flip()

    print('Splash Screen!')
    time.sleep(5)

class fish:
    def __init__ (self, screen, color):
        # Create a single fish
        fish_name = f'assests/sprites/{color}_fish.png'
        self.fish_img = pygame.image.load(fish_name).convert()
        self.fish_img.set_colorkey((0,0,0)) # makes area around fish transparent
        self.fish_x = random.randint(0,screen.get_width() - self.fish_img.get_width())
        self.fish_x_dir = 1
        self.fish_x_speed = screen.get_width()/(5*60)
        self.fish_y = random.randint(0,screen.get_width() - 4*self.fish_img.get_height())
        self.fish_y_dir = 1
        self.fish_y_speed = screen.get_height()/(5*60)

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

class C_Fish(fish):
    def __init__(self, screen, color):

        # Inherits everything from fish class
        super().__init__(screen, color)

    def update_position(self, screen):

        # Draw fish
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))
