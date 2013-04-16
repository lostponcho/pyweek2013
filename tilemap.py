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

    def add_box(self, x, y, w, h, tile_name):
        """Add a box of a given tile to the map.
        """
        tile = self.tileset.tiles[tile_name]
        
        for i in range(w):
            self.tiles[i][y] = tile
            self.tiles[i][y + h - 1] = tile 
            
        for i in range(h):
            self.tiles[x][i] = tile
            self.tiles[x + w - 1][i] = tile 
        
    def add_edge_wall(self, tile_name):
        """Add walls to edge.
        """
        self.add_box(0, 0, self.w, self.h, tile_name)
        
    def collide(self, rect, dx, dy):
        """Tests for collision with the tilemap.
        Should not collide with a tile if entity is already inside that tile. (So we don't get stuck)
        """

        if dx == 0 and dy == 0:
            return 0, 0
        
        x, y, w, h = rect

        # Handle largest movement first - means if we angle towards a corner, we will move to the
        # side that we are moving towards, not always biased to horizontal movement

        # Handle x movement
        if dx > 0:
            # X range to the right
            # From smallest to largest, so we stop as early as possible
            for tile_x in range(int((x + w) / self.tile_w) + 1,
                                int((x + w + dx) / self.tile_w) + 1):

                # Y range in centre             
                for tile_y in range(int(y / self.tile_h),
                                    int((y + h) / self.tile_h) + 1):

                    # This actually seems right, I can't even fucking believe it
                    if self.tiles[tile_x][tile_y].is_blocked:
                        # Keep dx limited to this value
                        x_to_be_hard_against = (tile_x - 1) * self.tile_w + self.tile_w
                        x_to_be_at = x_to_be_hard_against - w - 1 # Possibly -1
                        print "%2dx%2d %2.2f %d %d %d %d" % (x/self.tile_w, y/self.tile_h, dx, x_to_be_at, x, tile_x, tile_y)
                        dx = x_to_be_at - x
                        break
                
        else:
            # X range to the left            
            for tile_x in range(int((x) / self.tile_w) - 1,
                                int((x + dx) / self.tile_w) - 1, -1):
                
                # Y range in centre 
                for tile_y in range(int(y / self.tile_h),
                                    int((y + h) / self.tile_h) + 1):

                    # This actually seems right, I can't even fucking believe it                    
                    if self.tiles[tile_x][tile_y].is_blocked:
                        # Keep dx limited to this value
                        x_to_be_hard_against = (tile_x + 1) * self.tile_w
                        x_to_be_at = x_to_be_hard_against # Possibly +1
                        print "%2dx%2d %2.2f %d %d %d %d" % (x/self.tile_w, y/self.tile_h, dx, x_to_be_at, x, tile_x, tile_y)                        
                        dx = x_to_be_at - x
                        break
            
        # TODO: Handle y movement

        return dx, dy

    def display(self, screen, camera):
        cx, cy, cw, ch = camera
        for i in xrange(max(0, cx / self.tile_w),
                        min((cx + cw) / self.tile_w + 1, len(self.tiles))):
            for j in xrange(max(0, cy / self.tile_h),
                            min((cy + ch) / self.tile_h + 1, len(self.tiles[i]))):
                screen.blit(self.tiles[i][j].image,
                            (i * self.tile_w - cx, j * self.tile_h - cy),
                            self.tiles[i][j].rect)

img_data = {
    "resources/testsheet.png" : { # "little dude" : (0, 0, 32, 32, False),
                                  "dark floor"  : (1, 0, 32, 32, False),
                                  "light floor" : (2, 0, 32, 32, False),
                                  "blue floor"  : (3, 0, 32, 32, False),
                                  "grass"       : (4, 0, 32, 32, False) },
    "resources/crackedfloor.png" : { "cracked floor" : (0, 0, 32, 32, False), },
    "resources/brickwall.png" : { "brick wall left" : (0, 0, 32, 32, True),
                                  "brick wall mid" : (1, 0, 32, 32, True),
                                  "brick wall right" : (2, 0, 32, 32, True), }    
    }

def load_tileset(tile_dict, default):
    d = {}
    for sheet_img, defs in tile_dict.iteritems():
        img = pygame.image.load(sheet_img).convert_alpha()
        for name, (x, y, w, h, is_blocked) in defs.iteritems():
            x, y = x * w, y * h
            d[name] = Tile(img, pygame.Rect(x, y, w, h), is_blocked)
    return TileSet(d, default)

# Test
if __name__ == '__main__':
    def centre(x, w, dx, tile_w):
        """Get the tiles that we already cover.
        """
        return range(int(x / tile_w),
                     int((x + w) / tile_w) + 1)

    def pos_x_collide(x, w, dx, tile_w):
        """Get the new tiles that will move over.
        """
        return range(int((x + w) / tile_w) + 1,
                     int((x + w + dx) / tile_w) + 1)

    def neg_x_collide(x, w, dx, tile_w):
        """Get the new tiles that will move over.
        """
        return range(int(x / tile_w) - 1,
                     int((x + dx) / tile_w) - 1, -1)
    print list(centre(0, 15, 10, 16))
    print list(centre(0, 15, 10, 10))
    print list(centre(0, 15, 20, 10))
    print list(centre(0, 15, 10, 5))
    print '---'
    print list(pos_x_collide(0, 15, 10, 16))
    print list(pos_x_collide(0, 15, 10, 10))
    print list(pos_x_collide(0, 15, 20, 10))
    print list(pos_x_collide(0, 15, 10, 5))
    print '---'
    print list(neg_x_collide(0, 15, 10, -16))
    print list(neg_x_collide(0, 15, 10, -10))
    print list(neg_x_collide(0, 15, 20, -10))
    print list(neg_x_collide(0, 15, 10, -5))
