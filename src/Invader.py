import pygame
from pygame import mixer
from random import randint
from src import Bullet

class Invader(pygame.sprite.Sprite):
    def __init__(self, posx, posy, distance, img):
        pygame.sprite.Sprite.__init__(self)

        self.invaderAImg = pygame.image.load(img)
        self.rect = self.invaderAImg.get_rect()

        self.listShoot = []
        self.shootSpeed = 5
        self.rect.top = posy
        self.rect.left = posx
        self.speed = 3

        self.shootRange = 99

        self.timeChange = 1

        self.right = True
        self.counter = 0
        self.maxDesc = self.rect.top + 40

        self.limitRight = posx + distance
        self.limitLeft =  posx - distance

        self.conquest = False

    def draw(self, surface):
        surface.blit(self.invaderAImg, self.rect)

    def behaviour(self, time):
        if self.conquest == False:
            self.__movement()
            self.__atack()

    def __movement(self):
        if self.counter < 3:
            self.__movementLateral()
        else:
            self.__descens()

    def __movementLateral(self):
        if self.right == True:
            self.rect.left = self.rect.left + self.speed
            if self.rect.left > self.limitRight:
                self.right = False

                self.counter += 1
        else:
            self.rect.left = self.rect.left - self.speed
            if self.rect.left < self.limitLeft:
                self.right = True
                #self.counter += 1

    def __descens(self):
        if self.maxDesc == self.rect.top:
            self.counter = 0
            self.maxDesc = self.rect.top + 40
        else:
            self.rect.top += 1

    def __atack(self):
        if (randint(0,100)> self.shootRange):
            self.__shoot()

    def __shoot(self):
        x, y = self.rect.center
        myBullet = Bullet.Bullet(x-15,y, "img/bullet2.png", False)
        self.listShoot.append(myBullet)
        bullet_sound = mixer.Sound('sounds/laser2.wav')
        bullet_sound.play()