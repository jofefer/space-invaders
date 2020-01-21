import pygame
from random import randint
import math
from pygame import mixer
from src import Spaceship
from src import Invader

# SETTINGS
MAX_X = 800
MAX_Y = 600
MUSIC_ON = False
background = pygame.image.load('img/background.png')

#GLOBAL VARIABLES
enemyList = []

#score
score_value = 0
textX = 10
textY = 10



def stopAll():
    for enemy in enemyList:
        for shoot in enemy.listShoot:
            enemy.listShoot.remove(shoot)
        enemy.conquest = True

def show_score(x, y, screen):
    font = pygame.font.Font('freesansbold.ttf', 32)
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))

def game_over_text(screen):
    # game over text
    over_font = pygame.font.Font('freesansbold.ttf', 64)
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def loadEnemies():

    posx = 100
    for x in range(1, 7):
        enemy = Invader.Invader(posx, 100, 40, 'img/invader.png')
        enemyList.append(enemy)
        posx = posx+100




def game():
    pygame.init()


    # Sounds
    if MUSIC_ON:
        mixer.music.load('sounds/background.wav')
        mixer.music.play(-1)

    screen = pygame.display.set_mode((MAX_X, MAX_Y))

    # Title and Icon
    pygame.display.set_caption("SpaceInvaders")
    icon = pygame.image.load('img/ufo.png')
    pygame.display.set_icon(icon)

    #background
    background = pygame.image.load('img/background.png')

    player = Spaceship.Spaceship()
    loadEnemies()

    clock = pygame.time.Clock()

    running = True
    menu = True
    playing = True

    while running:

        while menu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        menu = False

            screen.fill((255,0,0))
            pygame.display.update()

        clock.tick(60)
        # change color of blackground (!!!probar a sacarlo fuera!!!!)
        screen.fill((0, 0, 0))
        screen.blit(background,(0,0))

        player.movement()


        time = pygame.time.get_ticks()/1000
        # events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.player_mov = -1*player.speed

                if event.key == pygame.K_RIGHT:
                    player.player_mov = player.speed
                if event.key == pygame.K_SPACE:
                    if playing:
                        x, y = player.rect.center
                        player.shoot(x-15, y-40)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player.player_mov = 0.0

        if player.player_mov < 0:
            player.rect.left += player.player_mov
        elif player.player_mov > 0:
            player.rect.right += player.player_mov

        player.draw(screen)




        if len(player.listShoot)> 0:
            for x in player.listShoot:
                x.draw(screen)
                x.traject()

                if x.rect.top < -10:
                    player.listShoot.remove(x)
                else:
                    for enemy in enemyList:
                        if x.rect.colliderect(enemy.rect):
                            enemyList.remove(enemy)
                            player.listShoot.remove(x)
                            global score_value
                            score_value = score_value + 1

        if len(enemyList)>0:
            for enemy in enemyList:
                enemy.draw(screen)
                enemy.behaviour(time)

                if enemy.rect.colliderect(player.rect):
                    player.destruction()
                    playing = False
                    stopAll()


                if len(enemy.listShoot)> 0:
                    for x in enemy.listShoot:
                        x.draw(screen)
                        x.traject()
                        if x.rect.colliderect(player.rect):
                            player.destruction()
                            playing = False
                            stopAll()

                        if x.rect.top > MAX_X +70:
                            enemy.listShoot.remove(x)

                        else:
                            for shoot in player.listShoot:
                                if x.rect.colliderect(shoot.rect):
                                    player.listShoot.remove(shoot)
                                    enemy.listShoot.remove(x)

        if playing == False:
            pygame.mixer.fadeout(3000)
            game_over_text(screen)

        show_score(10, 10, screen)
        pygame.display.update()

game()