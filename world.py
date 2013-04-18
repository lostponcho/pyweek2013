class World(object):
    """Contains all entity lists for updates, and the tilemaps.
    """

    def __init__(self, tilemap):
        self.tilemap = tilemap

        # Special lists for ai entities?
        self.ai_entities = set()
        self.display_entities = set()
        
        # Possibly split into several different lists
        # i.e. collision groups
        self.physics_entities = set()

        
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
