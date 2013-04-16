# Manage resources here

import animation

sounds = {}
images = {}
animations = {}

loaded_resources = False

def load_resources():
    """Fills the structure above with the resources for the game.
    """
    if loaded_resources:
        return
    loaded_resources = True
    
