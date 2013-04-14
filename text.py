import pygame
from pygame.locals import *

class Text(object):
    def __init__(self, x=0, y=0, font=None, text="", color=(255, 255, 255)):
        self.font = font
        self.text = text
        self.color = color
        self.pos = (x, y, 0, 0)
        self.render()

    def set_text(self, text):
        self.text = text
        self.render()

    def set_color(self, color):
        self.color = color
        self.render()

    def move(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def center_x(self, x1, x2):
        _, _, w, _ = self.pos
        self.pos.x = (x2 - x1) / 2 - (w / 2)

    def center_y(self, y1, y2):
        _, _, _, h = self.pos
        self.pos.y = (y2 - y1) / 2 - (h / 2)
        
    def get_rect(self):
        return self.pos
        
    def render(self):
        self.surface = self.font.render(self.text, True, self.color)
        x, y, _, _ = self.pos
        self.pos = self.surface.get_rect(x=x, y=y)
    
    def display(self, surface):
        surface.blit(self.surface, self.pos)
        
