import pygame
import random
import math

from pygame import mixer


pygame.init()


# Creat display window
screen = pygame.display.set_mode((800, 600))

# Background 
background =  pygame.image.load('background.png')

# Background Sound
mixer.music.load('background.wav')
mixer.music.play(-1)

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


# Bullet 
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480

bulletX_change = 0
bulletY_change = 10
bulletState = "ready"

def fireBullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x+16, y+10))


# Collision
def isCollision(enemy1X,enemy1Y,bulletX,bulletY):
    distance = math.sqrt(math.pow((enemy1X- bulletX), 2) + math.pow((enemy1Y - bulletY), 2))
    if distance < 27:
        return True
    else:
        return False


# Enimy_1
enemyImg1 = []
enemy1X = []
enemy1Y = []

enemy1X_change = []
enemy1Y_change = []

numOfEnemys = 6

for i in range(numOfEnemys):
    enemyImg1.append (pygame.image.load('ufo_1.png'))
    enemy1X.append(random.randint(30, 736))
    enemy1Y.append(random.randint(0, 100))
    enemy1X_change.append(1.5)
    enemy1Y_change.append(20)

def enemy_1(x, y, i):
    screen.blit(enemyImg1[i], (x, y))


# Enimy_2
enemyImg2 = pygame.image.load('ufo_2.png')
enemy2X = 370
enemy2Y = 480

enemy2X_change = 0


# Score board
scoreValu = 0
font = pygame.font.Font('Spicy Sale.ttf', 32)

textX =10
textY = 10

def showScore(x, y):
    score = font.render("Score : " + str(scoreValu), True, (255, 255, 255))
    screen.blit(score, (x, y))
# Game Loop
running = True

while running :

    # RGB  (Clore of the screen)
    screen.fill((0,0,0,))

    # Background Img
    screen.blit(background,(0,0))
    

    for event in pygame.event.get():


        # Close Window
        if event.type == pygame.QUIT:
            running = False

        # Player Movement
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -2

            if event.key == pygame.K_RIGHT:
                playerX_change = 2

            if event.key == pygame.K_SPACE:
                if bulletState is "ready":
                    bulletSound = mixer.Sound('laser.wav')
                    bulletSound.play()
                    bulletX = playerX
                    fireBullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    # Player Boundary       
    playerX += playerX_change

    if playerX <= 0 :
        playerX = 0
    if playerX >= 736 :
        playerX = 736


    # Bullet movement 
    if bulletY <= 0:
        bulletY = 480
        bulletState = "ready"

    if bulletState is "fire":
        fireBullet(bulletX, bulletY)
        bulletY -= bulletY_change


    # Enemy Boundary      
    for i in range(numOfEnemys):
        enemy1X[i] += enemy1X_change[i]
        if enemy1X[i] <= 0 :
            enemy1X_change[i] = 1.5
            enemy1Y[i] += enemy1Y_change[i]
        elif enemy1X[i] >= 736 :
            enemy1X_change[i] = -1.5
            enemy1Y[i] += enemy1Y_change[i]
   
        # Collision 
        collision = isCollision(enemy1X[i],enemy1Y[i],bulletX,bulletY)
        if collision:
            collisionSound = mixer.Sound('explosion.wav')
            collisionSound.play()
            bulletY = 480
            bulletState = "ready"
            scoreValu += 1
            print(scoreValu)
            enemy1X[i] = random.randint(30, 736)
            enemy1Y[i] = random.randint(0, 100)

        enemy_1(enemy1X[i], enemy1Y[i], i)


    player(playerX, playerY)

    showScore(textX, textY)

    pygame.display.update()
