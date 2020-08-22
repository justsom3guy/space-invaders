import pygame


class Enemy():
    def __init__(self, screenX, screenY):
        self.enemyIMG = pygame.image.load('assets/imgs/alien.png')
        self.screenX = screenX
        self.screenY = screenY
        self.posX = int(self.screenX/2)
        self.posY = int(self.screenY * .10)
        self.move_dist = 5

    def move_left(self):
        if self.posX - self.move_dist > 0:
            self.posX -= self.move_dist

    def move_right(self):
        if self.posX + self.move_dist < self.screenX:
            self.posX += self.move_dist

    def reset(self):
        self.posX = int(self.screenX/2)
        self.posY = int(self.screenY * .25)
