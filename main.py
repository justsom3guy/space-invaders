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
score_val = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)
scoreX = 10
scoreY = 10


def render_score(x, y):
    score = score_font.render(f'Score : {score_val}', True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game over
game_over_font = pygame.font.Font('freesansbold.ttf', 100)
game_over_posX = 100
game_over_posY = 200
game_over = False


def render_game_over(x, y):
    game_over = game_over_font.render('Game Over', True, (255, 255, 255))
    screen.blit(game_over, (x, y))


# Enemy
enemies = []
for i in range(0, 6):
    enemies.append(Enemy(screenX, screenY))


# Collision check
def collision(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dist < 30:
        return True
    return False


# Game loop
running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    screen.blit(player.playerIMG, (player.posX, player.posY))
    render_score(scoreX, scoreY)

    for enemy in enemies:
        screen.blit(enemy.enemyIMG, (enemy.posX, enemy.posY))
        if enemy.direction == "right":
            if enemy.posX + 50 > screenX:
                enemy.change_direction()
                enemy.move_down()
            enemy.move_right()
        else:
            if enemy.posX < 10:
                enemy.change_direction()
                enemy.move_down()
            enemy.move_left()

        if enemy.posY >= 450:
            game_over = True
            enemies.clear()

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

        for enemy in enemies:
            if collision(bullet.posX, bullet.posY, enemy.posX, enemy.posY):
                score_val += 1
                enemy.reset()
                if len(bullets):
                    bullets.remove(bullet)

    if game_over:
        render_game_over(game_over_posX, game_over_posY)

    pygame.display.update()
