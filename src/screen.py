# Initializes a few constant variables with the width and length of the screen

import pygame


# Initializes the screen
def initScreen(x, y):
    global SCR_SURFACE, SCR_WIDTH, SCR_HEIGHT
    pygame.display.init()
    SCR_SURFACE = pygame.display.set_mode((x, y))
    SCR_WIDTH = SCR_SURFACE.get_width()
    SCR_HEIGHT = SCR_SURFACE.get_height()






    

 