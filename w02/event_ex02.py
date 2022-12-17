import pygame,sys
from pygame.locals import *
pygame.init()
screen= pygame.display.set_mode((1000,1000))
red = 255
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == KEYUP:
            if event.key == K_DOWN:
               if red >= 20:
                 red -= 20
               else:
                 red = 255
            elif event.key == K_SPACE:
                red = 255
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
             pygame.quit()
             sys.exit()
    screen.fill((red,0,0))
    pygame.display.update()
