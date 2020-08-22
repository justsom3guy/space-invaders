import pygame
from entities.bullet import Bullet


class Player():
    def __init__(self, screenX, screenY):
        self.playerIMG = pygame.image.load('assets/imgs/spaceship.png')
        self.screenX = screenX
        self.screenY = screenY
        self.posX = int(self.screenX/2)
        self.posY = int(self.screenY * .85)
        self.move_dist = 20

    def move_left(self):
        if self.posX - self.move_dist > 0:
            self.posX -= self.move_dist

    def move_right(self):
        if self.posX + self.move_dist < self.screenX:
            self.posX += self.move_dist

    def shoot(self):
        bullet = Bullet(self.posX, self.posY)
        bullet.play_sound()
        return bullet
