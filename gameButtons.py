import pygame
pygame.init()
class Tile:
    button_color = (255, 255, 255)
    button_hover_color = (200, 200, 200)
    button_rect
    button_font = pygame.font.SysFont(None, 36)
    def __init__(self,x,y):
        global button_rect
        button_rect = pygame.Rect(x, y, 10, 10)