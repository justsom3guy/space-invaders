import pygame


class Bullet():
    def __init__(self, posX, posY):
        self.bulltImg = pygame.image.load('assets/imgs/bullet.png')
        self.posX = posX
        self.posY = posY

    def moveup(self):
        self.posY -= 10
