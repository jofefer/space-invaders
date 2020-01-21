import pygame
from pygame import mixer
from src import Bullet

MAX_X = 800
MAX_Y = 600

class Spaceship(pygame.sprite.Sprite):

    def __init__(self):
        self.shipImg = pygame.image.load('img/ship.png')
        self.rect = self.shipImg.get_rect()
        self.rect.centerx = MAX_X/2
        self.rect.centery = MAX_Y-30

        self.listShoot = []
        self.alive = True

        self.speed = 10
        self.player_mov = 0

    def movement(self):
        if self.alive:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right > MAX_X:
                self.rect.right = MAX_X

    def shoot(self, x, y):
        myBullet = Bullet.Bullet(x,y, "img/bullet.png", True)
        self.listShoot.append(myBullet)
        bullet_sound = mixer.Sound('sounds/laser.wav')
        bullet_sound.play()

    def draw(self, surface):
        surface.blit(self.shipImg, self.rect)

    def destruction(self):
        self.alive = False
        self.speed = 0
