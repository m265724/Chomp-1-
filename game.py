import pygame

print(f"Running make_screen.py")

#Screen dimensions
screen_width = 800
screen_height = 600

#Colors
blue = (0,0,255)
brown = (139,69,19)

#Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Blue Background with Brown Rectangle")

#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Fill screen with blue
    screen.fill(blue)

    #Draw brown rectangle
    rectangle_height = 100
    pygame.draw.rect(screen, brown, (0 ,screen_height - rectangle_height, screen_width, rectangle_height))

    #Update the display
    pygame.display.flip()

#Quit
pygame.quit()

print(f"End of code")