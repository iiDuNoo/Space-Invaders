#main.py for space invaders game
import pygame
import random

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
enemyImage = pygame.image.load('enemy.png')
enemyX= random.randint(0,800)
enemyY= random.randint(50,100)
enemyX_change = 4
enemyY_change = 35

#Bomb
#Ready - not seen on screen
#Fired - in motion
bombImage = pygame.image.load('bomb.png')
bombX= 0
bombY= 490
bombX_change = 0
bombY_change = 10
bomb_state = "ready"

def player(x,y):
    screensize.blit(playerImage,(x,y))

def enemy(x,y):
    screensize.blit(enemyImage,(x,y))

def fire_bomb(x,y):
    global bomb_state
    bomb_state = "fire"
    screensize.blit(bombImage,(x + 16,y + 10)) #padding from ship

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
                    bombX = playerX
                    fire_bomb(bombX,bombY)
                    
                bombX = playerX
                fire_bomb(bombX,bombY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #keyboard
                playerX_change = 0


    # updates player/enemy movement
    playerX += playerX_change
    enemyX += enemyX_change

#X boundary for player
    if playerX <= 0:
        playerX = 0

    elif playerX >= 736:
        playerX = 736

#X boundary for enemy
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 736:
            enemyX_change = -4
            enemyY += enemyY_change

#bomb movement
    if bombY <= 0:
        bombY = 480
        bomb_state = "ready"

    if bomb_state is "fire":
        fire_bomb(bombX, bombY)
        bombY -= bombY_change


    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update() #game is always updating screen
