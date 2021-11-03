import pygame

# Pygame initialization
pygame.init()

#  creating the screen
width = 626
height = 416
screen = pygame.display.set_mode((width, height))

# Caption and logo
pygame.display.set_caption("BUG OUTBREAK")
icon = pygame.image.load('images/fly.png')
pygame.display.set_icon(icon)

#Background Image
forest = pygame.image.load('images/forest.jpg')

# Important variables and co-ordinates
ychange = 0
sprite_num =1
x_cor = 75
y_cor = 200

# Game sprites
uzi = pygame.image.load('images/uzi.png')
bug_spray = pygame.image.load('images/bug-spray.png')
shotgun = pygame.image.load('images/shotgun.png')
worm = pygame.image.load('images/worm.png')
earthworm = pygame.image.load('images/earthworm.png')
fly_enemy = pygame.image.load('images/fly_enemy.png')
beetle =  pygame.image.load('images/beetle.png')

# Main Game loop
running = True
while running:

    # Drawing the background
    screen.blit(forest, (0,0))

    for event in pygame.event.get():
        # Closing the game window
        if event.type == pygame.QUIT:
            running = False
        # Key is pressed
        if event.type ==  pygame.KEYDOWN:
            # Changing the weapon
            if event.key == pygame.K_w:
                if sprite_num <= 3:
                    sprite_num += 1
                if sprite_num > 3:
                    sprite_num = 1
            # Taking the key responses
            elif event.key == pygame.K_UP:
                ychange = -0.1
            elif event.key == pygame.K_DOWN:
                ychange = +0.1
        # Key is realeased
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ychange = 0

    # Changin the weapons
    if sprite_num == 1:
        screen.blit(uzi, (x_cor, y_cor))
    elif sprite_num == 2:
        screen.blit(bug_spray, (x_cor, y_cor))
    else:
        screen.blit(shotgun, (x_cor, y_cor))

    # Changing the y co-ordinate and setting the boundaries
    y_cor += ychange
    if y_cor <= 0:
        y_cor = 0
    elif y_cor >= 354:
        y_cor = 354
    
    # Updating the window
    pygame.display.update()