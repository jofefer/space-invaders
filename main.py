import pygame
import random
import math
from pygame import mixer


# init the pygame
pygame.init()

# SETTINGS
MAX_X = 800
MAX_Y = 600
ENEMY_SPEED = 3.5
BULLET_SPEED = 7

background = pygame.image.load('img/background.png')

# Sounds
mixer.music.load('sounds/background.wav')
mixer.music.play(-1)

# create the screen
screen = pygame.display.set_mode((MAX_X, MAX_Y))

# Title and Icon
pygame.display.set_caption("SpaceInvaders")
icon = pygame.image.load('img/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/ship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('img/invader.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(ENEMY_SPEED)
    enemyY_change.append(40)

# Bullet - (Ready -> you can't see the bullet on the screen
#          (Fire -> You can see the bullet
bulletImg = pygame.image.load('img/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = BULLET_SPEED
bullet_state = "ready"

#score
score_value = 0
textX = 10
textY = 10
font = pygame.font.Font('freesansbold.ttf',32)

#game over text
over_font = pygame.font.Font('freesansbold.ttf',64)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# game Loop
running = True
while running:
    # change color of blackground
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))

    # events in the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5

            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0

    # Player boundaries movement
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= (MAX_X - 64):
        playerX = MAX_X - 64

    #Enemy boundaries movement
    for i in range(num_of_enemies):

        if enemyY[i] > 480:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = ENEMY_SPEED
            enemyY[i] += enemyY_change[i]

        elif enemyX[i] >= (MAX_X - 64):
            enemyX_change[i] = -ENEMY_SPEED
            enemyY[i] += enemyY_change[i]

        # collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #bullet movement
    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
