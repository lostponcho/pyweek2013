import tilemap
import resourcemanager

class World(object):
    """Contains all entity lists for updates, and the tilemaps.
    """
    def __init__(self, tilemap):
        self.tilemap = tilemap

        self.entities = []
        
        # Special lists for ai entities?
        self.ai_entities = set()
        self.display_entities = set()
        
        # Possibly split into several different lists
        # i.e. collision groups
        self.physics_entities = set()


    def add_entity(self, entity):
        self.entities.append(entity)
        
    def update(self):
        """Do this within entities?
        """
        for ai in self.ai_entities:
            ai.update()
        for animation in self.display_entities:
            animation.update()
        for physics in self.physics_entities:
            physics.update()

#        collision_check?
#        delete dead entities?
#        physics response?


def make_default_world():
    map = tilemap.TileMap(resourcemanager.tiles, "grass", 80, 60, 32, 32)
    map.random_fill(resourcemanager.tilesets["generation"])
    map.add_circle(60, 10, 10, "grass")
    map.add_circle(50, 20, 10, "grass")
    map.add_circle(70, 20, 10, "grass")
    map.add_filled_box(60, 0, 20, 20, "castle floor")
    map.add_circle(10, 45, 10, "dark floor")
    map.add_circle(10, 45, 5, "cracked floor")
    map.add_circle(5, 35, 5, "cracked floor")
    map.add_line(60, 59, 40, 30, "brick wall 0000")
    map.add_line(61, 59, 41, 30, "brick wall 0000")
    map.add_line(0, 20, 30, 50, "brick wall 0000")
    map.add_line(1, 20, 31, 50, "brick wall 0000")
    map.add_edge_wall("brick wall 0000")
    map.add_line(60, 10, 70, 10, "castle wall 0000")
    map.add_box(60, 0, 20, 20, "castle wall 0000")
    map.add_filled_box(60, 17, 3, 3, "castle floor")
    map.fix_brick_walls()
    world = World(map)
    return world
