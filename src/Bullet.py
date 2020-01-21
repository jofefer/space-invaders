import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, posx, posy, rute, character):
        pygame.sprite.Sprite.__init__(self)

        self.bulletImg = pygame.image.load(rute)
        self.rect = self.bulletImg.get_rect()

        self.shootSpeed = 5
        self.rect.top = posy
        self.rect.left = posx

        self.shootCharacter = character

    def traject(self):
        if self.shootCharacter == True:
            self.rect.top = self.rect.top - self.shootSpeed
        else:
            self.rect.top = self.rect.top + self.shootSpeed
    def draw(self, surface):
        surface.blit(self.bulletImg, self.rect)