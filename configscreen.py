import pygame

pygame.init()

config_screen_rect = pygame.Rect(170, 100, 660, 400)

def draw_config():
    pygame.draw.rect(pygame.display.get_surface(),(40, 40, 40), config_screen_rect)
    pygame.draw.rect(pygame.display.get_surface(),(80, 80, 80), config_screen_rect, 10)
