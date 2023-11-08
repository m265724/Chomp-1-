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


def make_splash_screen(background, scr):
    custom_font = pygame.font.Font('assets/fonts/Black_Crayon.ttf', 128)
    text = custom_font.render('Chomp', False, (255, 69, 0))
    scr.blit(background, (0, 0))
    scr.blit(text, (scr.get_width() / 2 - text.get_width() / 2, scr.get_height() / 2 - text.get_height() / 2 - 50))
    pygame.display.flip()

    print('Splash Screen!')
    time.sleep(5)


class Fish:
    def __init__(self, screen, color):
        # Create a single fish
        fish_name = f'assets/sprites/{color}_fish.png'
        self.fish_img = pygame.image.load(fish_name).convert()

        # makes area around fish transparent
        self.fish_img.set_colorkey((0, 0, 0))

        # Defines fish movement
        self.fish_x = random.randint(0, screen.get_width() - self.fish_img.get_width())
        self.fish_x_dir = 1
        self.fish_x_speed = screen.get_width()/(5*60)
        self.fish_y = random.randint(0, screen.get_width() - 4*self.fish_img.get_height())
        self.fish_y_dir = 1
        self.fish_y_speed = screen.get_height()/(5*60)

    # Updates fish position
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
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))

    # Checks for collisions
    def collision_check(self, other_fish):
        list_of_other_fish = []

        for Fish in other_fish:
            list_of_other_fish.append(pygame.Rect(Fish.fish_x, Fish.fish_y,
                                                  int(Fish.fish_img.get_width())/1.2,
                                                  int(Fish.fish_img.get_height())/1.2))

        my_bubble = pygame.Rect(self.fish_x, self.fish_y, int(self.fish_img.get_width())/1.2,
                                int(self.fish_img.get_height())/1.2)

        indices0 = my_bubble.collidelistall(list_of_other_fish)

        print(indices0)

        # Slows time when collision occurs (could be used to end game if collision occurs?)
        # if len(indices0) > 0:
            # time.sleep(3)


class C_Fish(Fish):
    def __init__(self, screen, color):

        # Inherits everything from fish class
        super().__init__(screen, color)

        # Keys
        self.key_up = "not pressed"
        self.key_down = "not pressed"
        self.key_left = "not pressed"
        self.key_right = "not pressed"

    def update_position(self, screen, events):

        # Update position w/ keystrokes
        for event in events:

            # Does something when a key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.key_up = "pressed"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.key_up = "not pressed"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.key_down = "pressed"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    self.key_down = "not pressed"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.key_left = "pressed"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.key_left = "not pressed"

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.key_right = "pressed"

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.key_right = "not pressed"

        # Update status based on keys
        if self.key_up == "pressed":
            self.fish_y -= self.fish_y_speed

        if self.key_down == "pressed":
            self.fish_y += self.fish_y_speed

        if self.key_left == "pressed":
            self.fish_x -= self.fish_x_speed

        if self.key_right == "pressed":
            self.fish_x += self.fish_x_speed

        # Create y bound
        # insert code

        # Create x bound
        # insert code

        # Draw fish
        screen.blit(self.fish_img, (self.fish_x, self.fish_y))
