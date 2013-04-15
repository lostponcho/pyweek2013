import pygame
from pygame.locals import *

import random

class Tile(object):
    """A tile definition.
    """
    def __init__(self, image, rect, is_blocked=False):
        self.image = image
        self.rect = rect
        self.is_blocked = is_blocked

class TileSet(object):
    """A tileset resource.
    """
    def __init__(self, tiles, default):
        self.tiles = tiles
        self.default = self.tiles[default]

class TileMap(object):
    """A tilemap that handles display and collision with tiles.
    """

    def __init__(self, tileset, w, h, tile_w, tile_h):
        self.tileset = tileset
        self.w, self.h = w, h
        self.tile_w, self.tile_h = tile_w, tile_h

        self.tiles = [[self.tileset.default
                       for _ in range(h)]
                      for _ in range(w)]

    def random_fill(self):
        tile_list = list(self.tileset.tiles.itervalues())
        
        for x in range(self.w):
            for y in range(self.h):
                self.tiles[x][y] = tile_list[random.randint(0, len(tile_list)-1)]
            

    def collide(self, rect, dx, dy):
        """Tests for collision with the tilemap.
        Should not collide with a tile if entity is already inside that tile. (So we don't get stuck)
        """

        if dx == 0 and dy == 0:
            return False
        
        x, y, w, h = rect

        # Handle largest movement first?

        # Handle x movement
        if dx > 0:
            # X range to the right
            for tile_x in range(int((x + w) / self.tile_w) + 1,
                                int((x + w + dx) / self.tile_w) + 1):

                # Y range in centre             
                for tile_y in range(int(y / self.tile_h),
                                    int((y + h) / self.tile_h) + 1):

                    # This calculation is wrong, what point is 0, 0 ?
                    if self.tiles[tile_x][tile_y].is_blocked:
                        # Keep dx limited to this value
                        dx = tile_x
                        break
                
        else:
            # X range to the left            
            for tile_x in range(int((x) / tile_w) - 1,
                                int((x + dx) / tile_w) - 1, -1):
                
                # Y range in centre 
                for tile_y in range(int(y / self.tile_h),
                                    int((y + h) / self.tile_h) + 1):

                    # This calculation is wrong, what point is 0, 0 ?
                    if self.tiles[tile_x][tile_y].is_blocked:
                        # Keep dx limited to this value
                        dx = tile_x
                        break
            
        # TODO: Handle y movement

    def display(self, screen, camera):
        cx, cy, cw, ch = camera
        for i in xrange(max(0, cy / self.tile_h),
                        min((cy + ch) / self.tile_h + 1, len(self.tiles))):
            for j in xrange(max(0, cx / self.tile_w),
                            min((cx + cw) / self.tile_w + 1, len(self.tiles[i]))):
                screen.blit(self.tiles[i][j].image,
                            (j * self.tile_w - cx, i * self.tile_h - cy),
                            self.tiles[i][j].rect)

img_data = {
    "resources/testsheet.png" : { # "little dude" : (0, 0, 32, 32, None),
                                  "dark floor"  : (1, 0, 32, 32, None),
                                  "light floor" : (2, 0, 32, 32, None),
                                  "blue floor"  : (3, 0, 32, 32, None),
                                  "grass"       : (4, 0, 32, 32, None) }
    }

def load_tileset(tile_dict, default):
    d = {}
    for sheet_img, defs in tile_dict.iteritems():
        img = pygame.image.load(sheet_img).convert_alpha()
        for name, (x, y, w, h, props) in defs.iteritems():
            x, y = x * w, y * h
            d[name] = Tile(img, pygame.Rect(x, y, w, h))
    return TileSet(d, default)

# Test
if __name__ == '__main__':
    def pos_x_collide(x, w, dx, tile_w):
        return range(int((x + w) / tile_w) + 1,
                     int((x + w + dx) / tile_w) + 1)

    def neg_x_collide(x, w, dx, tile_w):
        return range(int((x) / tile_w) - 1,
                     int((x + dx) / tile_w) - 1, -1)

    print list(pos_x_collide(0, 15, 10, 16))
    print list(pos_x_collide(0, 15, 10, 10))
    print list(pos_x_collide(0, 15, 20, 10))
    print list(pos_x_collide(0, 15, 10, 5))
    print '---'
    print list(neg_x_collide(0, 15, 10, -16))
    print list(neg_x_collide(0, 15, 10, -10))
    print list(neg_x_collide(0, 15, 20, -10))
    print list(neg_x_collide(0, 15, 10, -5))
