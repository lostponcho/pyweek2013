import pygame
from pygame.locals import *

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

    def collide(self, rect, dx, dy):
        """Tests for collision with the tilemap.
        Should not collide with a tile if entity is already inside that tile. (So we don't get stuck)
        """

        x, y, w, h = rect

        # Handle largest movement first?

        # Handle x movement
        if dx > 0:
            xr = range(int((x + w) / self.tile_w) + 1,
                       int((x + w + dx) / self.tile_w) + 1)
        else:
            xr = range(int((x) / tile_w) - 1,
                       int((x + dx) / tile_w) - 1, -1)
        # Handle y movement

    def display(self, screen, camera):
        w, h = self.tileset.get_size()
        cx, cy = int(camera.x * self.camera_mult), int(camera.y * self.camera_mult)
        for i in xrange(max(0, cy / h), min((cy + camera.h) / h + 1, len(self.tiles))):
            for j in xrange(max(0, cx / w), min((cx + camera.w) / w + 1, len(self.tiles[i]))):
                self.tileset.display(screen,
                                     self.tiles[i][j],
                                     (j * w - camera.x * self.camera_mult,
                                      i * h - camera.y * self.camera_mult))

img_data = {
    "resources/testsheet.png" : { "little dude" : (0, 0, 32, 32, None),
                                  "dark floor"  : (1, 0, 32, 32, None),
                                  "light floor" : (2, 0, 32, 32, None),
                                  "blue floor"  : (3, 0, 32, 32, None),
                                  "grass"       : (4, 0, 32, 32, None) }
    }

def load_tileset(tile_dict, default):
    d = {}
    for sheet_img, defs in tile_dict.iteritems():
        img = pygame.image.load(sheet_img).convert_alpha()
        for name, (x, y, w, h, props) in defs:
            x, y = x * w, y * h
            d[name] = Tile(img, pygame.Rect(x, y, w, h))
    return Tileset(d, default)

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
