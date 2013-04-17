import pygame

class Camera(object):
    """Keeps the player in the centre half of the screen.
    """
    def __init__(self, screen_width, screen_height, world_width, world_height):
        self.width, self.height = world_width, world_height
        self.pos = pygame.Rect(0, 0, screen_width, screen_height)

    def update(self, x, y):
        """Update the camera with the x,y of the player.
        """
        cx, cy, cw, ch = self.pos
        
        if x < cx + cw/3:
            self.pos.x = max(0, x - cw/3)

        elif x > cx + cw*2/3:
            self.pos.x = min(self.width - cw, x - cw * 2/3)
            
        if y < cy + ch/3:
            self.pos.y = max(0, y - ch/3)

        elif y > cy + ch*2/3:
            self.pos.y = min(self.height - ch, y - ch * 2/3)
    
