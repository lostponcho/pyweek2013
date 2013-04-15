class Tile(object):
    """A tile definition.
    """
    def __init__(self, image, blocked=False):
        self.image = image
        self.blocked = blocked

class TileSet(object):
    """A tileset resource.
    """
    def __init__(self, w, h, tiles):
        self.default = 0
        self.tiles = tiles
        self.tile_w, self.tile_h = tiles[0].image.size

    def blocked(self, i):
        return self.tiles[i].blocked

class TileMap(object):
    """A tilemap that handles display and collision with tiles.
    """

    def __init__(self, tileset, w, h):
        self.tileset = tileset
        self.w, self.h = w, h

        self.tiles = [[self.tileset.default
                       for _ in range(h)]
                      for _ in range(w)]

        self.tile_w, self.tile_h = self.tileset.get_tile_size()

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
