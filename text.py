import pygame
from pygame.locals import *

class Text(object):
    def __init__(self, x=0, y=0, font=None, text="", color=(255, 255, 255), background=None, alpha=None):
        self.font = font
        self.text = text
        self.color = color
        self.background = background
        self.alpha = alpha
        self.pos = (x, y, 0, 0)
        self.render()

    def set_text(self, text):
        self.text = text
        self.render()

    def set_color(self, color):
        self.color = color
        self.render()

    def set(self, x, y):
        self.pos.x = x
        self.pos.y = y

    def move(self, dx, dy):
        self.pos.x += dx
        self.pos.y += dy

    def center_x(self, x1, x2):
        _, _, w, _ = self.pos
        self.pos.x = (x2 - x1) / 2 - (w / 2)

    def center_y(self, y1, y2):
        _, _, _, h = self.pos
        self.pos.y = (y2 - y1) / 2 - (h / 2)
        
    def get_rect(self):
        return self.pos
        
    def render(self):
        if self.background is not None:
            self.surface = self.font.render(self.text, True, self.color, self.background)
        else:
            self.surface = self.font.render(self.text, True, self.color)
        if self.alpha is not None:
            self.surface.set_alpha(self.alpha)
        x, y, _, _ = self.pos
        self.pos = self.surface.get_rect(x=x, y=y)
    
    def display(self, surface):
        surface.blit(self.surface, self.pos)

