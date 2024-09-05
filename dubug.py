import pygame

pygame.init()
font = pygame.font.Font(None, 30)
light_grey = (180, 180, 180)


def debugger(info, x = 10, y = 10,color = light_grey):
    display_surf = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, color)
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    display_surf.blit(debug_surf, debug_rect)
