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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    player(playerX,playerY)
    pygame.display.update() #game is always updating screen
