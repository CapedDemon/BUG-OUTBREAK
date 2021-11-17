import pygame
import random
import math
from pygame import mixer

# Pygame initialization and main loop variable
running = True
pygame.init()

#  creating the screen
width = 626
height = 416
screen = pygame.display.set_mode((width, height))

# Caption and logo
pygame.display.set_caption("BUG OUTBREAK")
icon = pygame.image.load('images/fly.png')
pygame.display.set_icon(icon)

# Background Image
forest = pygame.image.load('images/forest.jpg')

# Important variables and co-ordinates for player
score = 0
ychange = 0
sprite_num = 1
x_cor = 75
y_cor = 200
result = False
result2 = False
result3 = False

# Enemy loading & Displaying
worm = []
fly_enemy = []
beetle = []

worm_x_cor = []
worm_y_cor = []
worm_x_change = []
worm_done = 0

beetle_x_cor = []
beetle_y_cor = []
beetle_x_change = []
beetle_y_change = []

fly_x_cor = []
fly_y_cor = []
fly_x_change = []
fly_y_change = []
fly_done = 0

num_worm = 5
num_fly_enemy = 5
num_beetle = 10
total_enemies = num_beetle + num_fly_enemy + num_worm
total_enemies_done = 0

# Game sprites
uzi = pygame.image.load('images/uzi.png')
bug_spray = pygame.image.load('images/bug-spray.png')
shotgun = pygame.image.load('images/shotgun.png')

# Bullet showing function
bullet_num = 1
bullet_state = "ready"
bullet_x = 0
bullet_y = 0


def show_bullet(x_cor_bullet, y_cor_bullet, bulletNum):
    global bullet_state
    bullet_state = "fire"
    if bulletNum == 1:
        screen.blit(pygame.image.load('images/uzi_bullet.png'),
                    (x_cor_bullet+50, y_cor_bullet))
    elif bulletNum == 2:
        screen.blit(pygame.image.load('images/smoke.png'),
                    (x_cor_bullet + 30, y_cor_bullet-40))
    elif bulletNum == 3:
        screen.blit(pygame.image.load('images/shotgun_bullet.png'),
                    (x_cor_bullet + 100, y_cor_bullet + 25))

# Collision function
def collisionDetect(enemyX, enemyY, bulletX, bulletY):
    d = math.sqrt((math.pow((enemyX - bulletX), 2)) +
                  (math.pow((enemyY - bulletY), 2)))
    if d < 27:
        return True
    else:
        return False


# Font and Game Over
font = pygame.font.Font('freesansbold.ttf', 82)
activate_over = True
def GameOver(x1, x, y):
    global running
    global activate_over
    if activate_over == False:
        if x1 < 75 and x1 > 0:
            text = font.render("GAME OVER", True, (225, 225, 225))
            screen.blit(text, (x, y))
            running = False


# Background Sound
if total_enemies != 0:
    mixer.music.load("musics/ES_Shinjuku - Leimoti.mp3")
    mixer.music.play()
else:
    mixer.music.load("musics/ES_Fights - AGST.mp3")
    mixer.music.play()

# Main Game loop
while running:

    # Drawing the background
    screen.blit(forest, (0, 0))

    for event in pygame.event.get():
        # Closing the game window
        if event.type == pygame.QUIT:
            running = False
        # Key is pressed
        if event.type == pygame.KEYDOWN:
            activate_over = False
            # Changing the weapon as well as changing the bullet
            if event.key == pygame.K_w:
                if sprite_num <= 3 and bullet_num <= 3:
                    if bullet_state == "ready":
                        sprite_num += 1
                        bullet_num += 1
                elif sprite_num > 3 and bullet_num > 3:
                    if bullet_state == "ready":
                        sprite_num = 1
                        bullet_num = 1

            # Taking the key responses
            elif event.key == pygame.K_UP:
                ychange = -20
            elif event.key == pygame.K_DOWN:
                ychange = 20

            # Bullet Appearance
            elif event.key == pygame.K_SPACE:
                bullet_x = x_cor
                bullet_y = y_cor
                bullet_num = sprite_num
                if bullet_state == "ready":
                    show_bullet(bullet_x, (bullet_y+5), bullet_num)

        # Key is realeased
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ychange = 0

    # Changing the weapons
    if sprite_num == 1:
        screen.blit(uzi, (x_cor, y_cor))

    elif sprite_num == 2:
        screen.blit(bug_spray, (x_cor, y_cor))

    else:
        screen.blit(shotgun, (x_cor, y_cor))

    # Changing the y co-ordinate and setting the boundaries of players
    y_cor += ychange
    if y_cor <= 0:
        y_cor = 0
    elif y_cor >= 354:
        y_cor = 354

    # Enemy Column
    # Making all the enemies by running a for loop of range of the total enemies

    for i in range(total_enemies):

        # Displaying the number of worms
        for worms in range(num_worm):
            worm.append(pygame.image.load('images/worm.png'))
            worm_x_cor.append(random.randint(500, 700))
            worm_y_cor.append(352)
            screen.blit(worm[worms], (worm_x_cor[worms], worm_y_cor[worms]))
            worm_x_change.append(0.2)
            # Moving in the x co-ordinate only
            worm_x_cor[worms] -= worm_x_change[worms]

            GameOver(worm_x_cor[worms], 10, 10)

        # Displaying the number of flies
        for flies in range(num_fly_enemy):
            fly_enemy.append(pygame.image.load('images/fly_enemy.png'))
            fly_x_cor.append(random.randint(500, 600))
            fly_y_cor.append(random.randint(0, 416))
            screen.blit(fly_enemy[flies], (fly_x_cor[flies], fly_y_cor[flies]))
            fly_x_change.append(65)
            fly_y_change.append(0.2)

            # Movement of the flies in the x co-ordinate as well as y co-ordinate
            fly_y_cor[flies] -= fly_y_change[flies]
            if fly_y_cor[flies] <= 0:
                fly_y_change[flies] = -0.2
                fly_x_cor[flies] -= fly_x_change[flies]
            elif fly_y_cor[flies] >= 352:
                fly_y_change[flies] = 0.2
                fly_x_cor[flies] -= fly_x_change[flies]

            GameOver(fly_x_cor[flies], 10, 10)

        # Displaying the number of beetles
        for beetles in range(num_beetle):
            beetle.append(pygame.image.load('images/beetle.png'))
            beetle_x_cor.append(random.randint(500, 600))
            beetle_y_cor.append(random.randint(0, 416))
            screen.blit(beetle[beetles],
                        (beetle_x_cor[beetles], beetle_y_cor[beetles]))
            beetle_x_change.append(65)
            beetle_y_change.append(0.2)

            # Movement of the beetles in the x co-ordinate as well as y co-ordinate
            beetle_y_cor[beetles] -= beetle_y_change[beetles]
            if beetle_y_cor[beetles] <= 0:
                beetle_y_change[beetles] = -0.2
                beetle_x_cor[beetles] -= beetle_x_change[beetles]
            elif beetle_y_cor[beetles] >= 352:
                beetle_y_change[beetles] = 0.2
                beetle_x_cor[beetles] -= beetle_x_change[beetles]

            GameOver(beetle_x_cor[beetles], 10, 10)

    # Bullet movement
    if bullet_x >= 626:
        bullet_x = x_cor
        bullet_state = "ready"
    if bullet_state == "fire":
        show_bullet(bullet_x, (bullet_y+5), bullet_num)
        bullet_x += 15

    # Collision
    for j in range(total_enemies):
        if sprite_num == 3:
            for worms in range(num_worm):
                result = collisionDetect(
                    worm_x_cor[worms], worm_y_cor[worms], bullet_x, bullet_y)
                if result == True:
                    score += 1
                    bullet_x = x_cor
                    bullet_y = y_cor
                    bullet_state = "ready"
                    print(score)
                    worm.pop(worms)
                    worm_x_cor.pop(worms)
                    worm_y_cor.pop(worms)
                    worm_x_change.pop(worms)
                    num_worm -= 1

        elif sprite_num == 2:
            for flies in range(num_fly_enemy):
                result2 = collisionDetect(
                    fly_x_cor[flies], fly_y_cor[flies], bullet_x, bullet_y)
                if result2 == True:
                    score += 1
                    bullet_x = x_cor
                    bullet_y = y_cor
                    bullet_state = "ready"
                    print(score)
                    fly_enemy.pop(flies)
                    fly_x_cor.pop(flies)
                    fly_y_cor.pop(flies)
                    fly_x_change.pop(flies)
                    fly_y_change.pop(flies)
                    num_fly_enemy -= 1

        elif sprite_num == 1:
            for beetles in range(num_beetle):
                result3 = collisionDetect(
                    beetle_x_cor[beetles], beetle_y_cor[beetles], bullet_x, bullet_y)
                if result3 == True:
                    score += 1
                    bullet_x = x_cor
                    bullet_y = y_cor
                    bullet_state = "ready"
                    print(score)
                    beetle.pop(flies)
                    beetle_x_cor.pop(flies)
                    beetle_y_cor.pop(flies)
                    beetle_x_change.pop(flies)
                    beetle_y_change.pop(flies)
                    num_beetle -= 1

    # Updating the window
    pygame.display.update()
