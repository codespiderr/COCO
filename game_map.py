import pygame
import Player
from map import game_map

pygame.init()

grass1 = pygame.image.load("pictures/grass/tile004.png")  # grass tile
grass1 = pygame.transform.scale(grass1, (64, 64))

flower1 = pygame.image.load("pictures/grass/tile252.png")  # small white flowers
flower1 = pygame.transform.scale(flower1, (64, 64))

flower2 = pygame.image.load("pictures/grass/tile306.png")  # big red flowers
flower2 = pygame.transform.scale(flower2, (64, 64))

mushroom1 = pygame.image.load("pictures/grass/tile337.png")  # mushroom
mushroom1 = pygame.transform.scale(mushroom1, (64, 64))

boundary1 = pygame.image.load("pictures/grass/tile042.png")  # pink boundary tile
boundary1 = pygame.transform.scale(boundary1, (64, 64))

crate = pygame.image.load("pictures/grass/crate.png")  # crate icon

grass = [grass1, grass1, grass1, grass1]

player_pos_obj = Player.Player(grass, grass, grass, grass, (-2560, -640), 10)


class tilemap():
    def __init__(self):
        self.game_screen = pygame.display.get_surface()
        self.tile_surface = pygame.Surface((7680, 2560))  # 6400,1920
        self.tile_surface.fill("white")
        self.x = 0
        self.y = 0

        self.offset_x_add = -2560
        self.offset_y_add = -640

        self.collision_block = False

        self.offsetx3 = 0
        self.offsety3 = 0

    def blitter(self):
        player_pos_obj.input()

        self.offset_x = -(player_pos_obj.direction[0] * player_pos_obj.speed)
        self.offset_y = -(player_pos_obj.direction[1] * player_pos_obj.speed)

        if self.offset_x_add + self.offset_x <= -6390 or self.offset_x_add + self.offset_x >= -5 or self.offset_y_add + self.offset_y <= -1880 or self.offset_y_add + self.offset_y >= 5:  # boundary checking
            self.offset_x_add += 0
            self.offset_y_add += 0
        else:
            self.offset_x_add += (self.offset_x - self.offsetx3)
            self.offset_y_add += (self.offset_y - self.offsety3)
            self.offsetx3 = 0
            self.offsety3 = 0

        self.y = 0
        for row in game_map:
            self.x = 0
            for tile in row:

                if tile == "g":  # tiles
                    self.tile_surface.blit(grass1, (self.x, self.y))
                if tile == "c":  # crates
                    self.tile_surface.blit(crate, (self.x, self.y))

                    self.player_rect = pygame.Rect((-self.offset_x_add + 615 + 3, -self.offset_y_add + 315), (51, 64))
                    self.crate_rect = pygame.Rect((self.x + 5, self.y + 5), (64 - 10, 64 - 10))

                    # pygame.draw.rect(self.tile_surface, (255, 0, 0), pygame.Rect(-(self.offset_x_add) + 615+3, -(self.offset_y_add) + 315, 51, 64))
                    if pygame.Rect.colliderect(self.crate_rect, self.player_rect):
                        # pygame.draw.rect(self.tile_surface, (100, 250, 0), pygame.Rect(self.x+5, self.y+5, 64-10, 64-10))
                        if self.offset_x > 0:
                            self.offsetx3 = 10
                        if self.offset_x < 0:
                            self.offsetx3 = -10

                        if self.offset_y > 0:
                            self.offsety3 = 10
                        if self.offset_y < 0:
                            self.offsety3 = -10

                if tile == "b":  # boundary tiles
                    self.tile_surface.blit(boundary1, (self.x, self.y))
                if tile == "f":  # flower 1 using grass background
                    self.tile_surface.blit(grass1, (self.x, self.y))
                    self.tile_surface.blit(flower1, (self.x, self.y))
                if tile == "F":  # flower 2
                    self.tile_surface.blit(grass1, (self.x, self.y))
                    self.tile_surface.blit(flower2, (self.x, self.y))
                if tile == "m":
                    self.tile_surface.blit(grass1, (self.x, self.y))
                    self.tile_surface.blit(mushroom1, (self.x, self.y))
                self.x += 64
            self.y += 64

    def update(self):

        self.blitter()
        self.game_screen.blit(self.tile_surface, (self.offset_x_add, self.offset_y_add))


tilemap_obj = tilemap()
