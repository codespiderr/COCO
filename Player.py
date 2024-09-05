import pygame

pygame.init()


class Player:
    def __init__(self, stat0, stat1, stat2, stat3, pos, speed=8):
        super().__init__()
        self.number = 0
        self.numero = int(self.number)
        self.picture_down = stat0  # player pictures
        self.picture_left = stat1
        self.picture_right = stat2
        self.picture_up = stat3
        self.image = self.picture_down[self.number]
        self.pos = pos
        self.rect = self.image.get_rect(topleft=pos)
        self.game_screen = pygame.display.get_surface()
        self.direction = pygame.math.Vector2()
        self.speed = speed

    def input(self):  # movement check
        keys = pygame.key.get_pressed()

        if self.number < (len(self.picture_down) - 0.2):
            self.number += 0.2
        else:
            self.number = 0

        self.numero = int(self.number)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.direction.y = -1
            self.image = self.picture_up[self.numero]
        elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.direction.y = 1
            self.image = self.picture_down[self.numero]
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.direction.x = 1
            self.image = self.picture_right[self.numero]
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.direction.x = -1
            self.image = self.picture_left[self.numero]
        else:
            self.direction.x = 0

    def update(self):
        self.input()  # calling movements
        self.rect.center += self.direction * self.speed  # multipling with speed
        self.game_screen.blit(self.image, self.rect.center)  # blitting with vector 2 coordinates
        self.pos = self.rect  # getting the player position
