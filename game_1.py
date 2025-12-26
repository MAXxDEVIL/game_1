import pygame
import random

pygame.init()


# Creat display window
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)


# Player
playerImg = pygame.image.load('rocket.png')
playerX = 370
playerY = 480

playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


# Enimy_1
enemyImg1 = pygame.image.load('ufo_1.png')
enemy1X = random.randint(30, 736)
enemy1Y = random.randint(0, 100)

enemy1X_change = 0
enemy1Y_change = 0

def enemy_1(x, y):
    screen.blit(enemyImg1, (x, y))


# Enimy_2
enemyImg2 = pygame.image.load('ufo_2.png')
enemy2X = 370
enemy2Y = 480

enemy2X_change = 0


# Game Loop
running = True

while running :

    # RGB  (Clore of the screen)
    screen.fill((0,0,0,))
    

    for event in pygame.event.get():


        # Close Window
        if event.type == pygame.QUIT:
            running = False

        # Player Movement
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -0.2

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

        # Enemy Movement

        
            
    # Player Boundary       
    playerX += playerX_change

    if playerX <= 0 :
        playerX = 0
    if playerX >= 736 :
        playerX = 736


    # Enemy Boundary       
    enemy1X += enemy1X_change
    
    if enemy1X <= 0 :
        enemy1X_change += 0.001
    if enemy1X >= 736 :
        enemy1X_change -= 0.001


    player(playerX, playerY)

    enemy_1(enemy1X, enemy1Y)

    pygame.display.update()
