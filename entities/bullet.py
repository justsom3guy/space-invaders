import pygame
from pygame import mixer


class Bullet():
    def __init__(self, posX, posY):
        self.bulltImg = pygame.image.load('assets/imgs/bullet.png')
        self.sound = mixer.Sound('assets/sounds/pew.wav')
        self.posX = posX+15
        self.posY = posY

    def moveup(self):
        self.posY -= 10

    def play_sound(self):
        self.sound.play()
