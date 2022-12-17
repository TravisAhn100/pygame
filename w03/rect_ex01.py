import pygame, sys
from pygame.locals import *

pygame.init()
width=1000
height = 1000
screen = pygame.display.set_mode((width,height))

r1=pygame.Rect(150,150,100,100)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),r1)
    pygame.display.update()
    



