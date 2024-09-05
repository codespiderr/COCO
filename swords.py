import time

import pygame
import math

sword1 = pygame.image.load("pictures/swords/weapons/weapon18v2.png")
sword1 = pygame.transform.scale(sword1, (96, 96))
sword1 = [sword1]

pygame.init()


class swords:
    def __init__(self):
        self.gamescreen = pygame.display.get_surface()
        self.pos = pygame.mouse.get_pos()

    def sword_update(self, events, sword):
        mouseclick = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseclick = True
        self.pos = pygame.mouse.get_pos()
        # if mouseclick:
        angle = 360 - math.atan2(self.pos[1] - 355, self.pos[0] - 645) * 180 / math.pi
        angle -= 35
        rotimage = pygame.transform.rotate(sword, angle)
        rect = rotimage.get_rect(center=(645, 355))
        self.gamescreen.blit(rotimage, rect)
        mouseclick = False
