import pygame
import random
import math
from pygame import mixer

# SETTINGS
MAX_X = 800
MAX_Y = 600
ENEMY_SPEED = 3.5
BULLET_SPEED = 7

background = pygame.image.load('img/background.png')

class spaceship(pygame.sprite.Sprite):

    def __init__(self):
        self.shipImg = pygame.image.load('img/ship.png')
        self.rect = self.shipImg.get_rect()
        self.rect.centerx = MAX_X/2
        self.rect.centery = MAX_Y-30

        self.listShoot = []
        self.alive = True

        self.speed = 20

    def movement(self):
        if self.alive:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > MAX_X:
                self.rect.right = MAX_X

    def shoot(self):
        print("Shooting")

    def draw(self, surface):
        surface.blit(self.shipImg, self.rect)


def game():
    pygame.init()
    screen = pygame.display.set_mode((MAX_X, MAX_Y))
    # Title and Icon
    pygame.display.set_caption("SpaceInvaders")
    icon = pygame.image.load('img/ufo.png')
    pygame.display.set_icon(icon)

    #background
    background = pygame.image.load('img/background.png')

    player = spaceship()

    running = True
    playing = True
    while running:
        # change color of blackground (!!!probar a sacarlo fuera!!!!)
        screen.fill((0, 0, 0))
        screen.blit(background,(0,0))

        player.movement()

        # events in the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.rect.left -= player.speed

                if event.key == pygame.K_RIGHT:
                    player.rect.right += player.speed
                if event.key == pygame.K_SPACE:
                    """  old code
                    if bullet_state is "ready":
                        bullet_sound = mixer.Sound('sounds/laser.wav')
                        bullet_sound.play()
                        bulletX = playerX
                        fire_bullet(bulletX, bulletY)
                    """
                    player.shoot()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0.0

        player.draw(screen)
        pygame.display.update()

game()