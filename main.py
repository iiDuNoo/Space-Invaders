#main.py for space invaders game
import pygame

#initialization of pygame
pygame.init()
screensize = pygame.display.set_mode((800,600)) #width x height

#Window Title and Picture
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('rocket.png')
pygame.display.set_icon(icon)

#Player
playerImage = pygame.image.load('player.png')
playerX=370 #about half 800
playerY=480
playerX_change = 0

def player(x,y):
    screensize.blit(playerImage,(x,y))

#loop to keep game running and update
running = True
while running:
    #colours RGB - stays black
    screensize.fill((0, 0, 0))

    #movement mechanics
    for event in pygame.event.get(): #any keystroke is an event ingame
        if event.type == pygame.QUIT:
            running = False
    #if keystroke is pressed, it will be recognized
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #left arrow
                playerX_change = -0.25
            if event.key == pygame.K_RIGHT: #right arrow
                playerX_change = 0.25
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #keyboard
                playerX_change = 0

    # updates player movement
    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update() #game is always updating screen
