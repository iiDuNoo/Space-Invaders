#main.py for space invaders game
import pygame
import random
import math

#initialization of pygame
pygame.init()
screensize = pygame.display.set_mode((800,600)) #width x height

#Background image
bg = pygame.image.load('background.png')

#Window Title and Picture
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImage = pygame.image.load('player.png')
playerX=370 #about half 800
playerY=490
playerX_change = 0

#Alien enemy
enemyImage = []
enemyX= []
enemyY= []
enemyX_change = []
enemyY_change = []
numberEnemy = 6

for i in range(numberEnemy):
    enemyImage.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append(35)

#Bomb
#Ready - not seen on screen
#Fired - in motion
bombImage = pygame.image.load('bomb.png')
bombX= 0
bombY= 490
bombX_change = 0
bombY_change = 10
bomb_state = "ready"

score =0

def player(x,y):
    screensize.blit(playerImage,(x,y))

def enemy(x,y,i):
    screensize.blit(enemyImage[i],(x,y))

def fire_bomb(x,y):
    global bomb_state
    bomb_state = "fire"
    screensize.blit(bombImage,(x + 16,y + 10)) #padding from ship

def isCollision(enemyX,enemyY,bombX,bombY):
    distance = math.sqrt(math.pow(enemyX - bombX, 2) + (math.pow(enemyY - bombY, 2)))
    if distance < 27:
        return True
    else:
        return False

#loop to keep game running and update
running = True
while running:
    #colours RGB - stays black
    screensize.fill((0, 0, 0))

    #background image refresh
    screensize.blit(bg,(0,0))

    #movement mechanics
    for event in pygame.event.get(): #any keystroke is an event ingame
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed, it will be recognized
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #left arrow
                playerX_change = -5
            if event.key == pygame.K_RIGHT: #right arrow
                playerX_change = 5
            if event.key == pygame.K_SPACE: #spacebar
                if bomb_state is "ready":
                    #finds current x coordinate for ship
                    bombX = playerX
                    fire_bomb(bombX,bombY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #keyboard
                playerX_change = 0


    # updates player/enemy movement
    playerX += playerX_change

#X boundary for player
    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

#X boundary for enemy
    for i in range(numberEnemy):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]

    #collision
        collision = isCollision(enemyX[i],enemyY[i],bombX,bombY)
        if collision:
            bombY = 480
            bomb_state = "ready"
            score+= 1
            print(score)
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i],enemyY[i], i)

#bomb movement
    if bombY <= 0:
        bombY = 480
        bomb_state = "ready"

    if bomb_state is "fire":
        fire_bomb(bombX, bombY)
        bombY -= bombY_change


    player(playerX,playerY)

    pygame.display.update() #game is always updating screen
