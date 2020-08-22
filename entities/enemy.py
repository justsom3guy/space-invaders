import pygame
import random
from pygame import mixer


class Enemy():
    def __init__(self, screenX, screenY):
        self.enemyIMG = pygame.image.load('assets/imgs/alien.png')
        self.hit_sound = mixer.Sound('assets/sounds/hit.wav')
        self.screenX = screenX
        self.screenY = screenY
        self.posX = random.randint(0, 800)
        self.posY = random.randint(50, 150)
        self.move_dist_x = 3
        self.move_dist_y = 40
        self.direction = random.choice(['right', 'left'])

    def change_direction(self):
        if self.direction == "right":
            self.direction = "left"
        else:
            self.direction = "right"

    def move_down(self):
        self.posY += self.move_dist_y

    def move_left(self):
        if self.posX - self.move_dist_x > 0:
            self.posX -= self.move_dist_x

    def move_right(self):
        if self.posX + self.move_dist_x < self.screenX:
            self.posX += self.move_dist_x

    def reset(self):
        self.posX = random.randint(0, 800)
        self.posY = random.randint(50, 300)
        self.hit_sound.play()
