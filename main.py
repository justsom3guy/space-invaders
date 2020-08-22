import math
import pygame
from entities.player import Player
from entities.enemy import Enemy

# Initialize the pygame
pygame.init()

# Create the screen
screenX = 800
screenY = 600
screen = pygame.display.set_mode((screenX, screenY))

# Backgorund
background = pygame.image.load('assets/imgs/background.png')

# Title and icon
icon = pygame.image.load('assets/imgs/ufo.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Space fighter')

# Player
player = Player(screenX, screenY)

# Bullets
bullets = []

# Score
score = 0

# Enemy
enemy_is_alive = True
enemy_direction = "right"
enemy = Enemy(screenX, screenY)


# Collision check
def collision(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dist < 20:
        return True
    return False


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))

    if enemy_is_alive:
        if enemy_direction == "right":
            if enemy.posX + 50 > screenX:
                enemy_direction = "left"
                enemy.posY += enemy.move_dist*10
            enemy.move_right()
        else:
            if enemy.posX < 10:
                enemy_direction = "right"
                enemy.posY += enemy.move_dist*10
            enemy.move_left()
    else:
        enemy.reset()
        enemy_is_alive = True

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                player.move_left()

            if event.key == pygame.K_RIGHT:
                player.move_right()

            if event.key == pygame.K_SPACE:
                bullets.append(player.shoot())

        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                player.move_left()

            if event.key == pygame.K_RIGHT:
                player.move_right()

    for bullet in bullets:
        screen.blit(bullet.bulltImg, (bullet.posX, bullet.posY))
        bullet.moveup()
        if bullet.posY - 10 < 10:
            bullets.remove(bullet)

        if collision(bullet.posX, bullet.posY, enemy.posX, enemy.posY):
            score += 1
            bullets.remove(bullet)

    print(score)

    screen.blit(player.playerIMG, (player.posX, player.posY))
    screen.blit(enemy.enemyIMG, (enemy.posX, enemy.posY))
    pygame.display.update()
