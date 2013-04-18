# Manage resources here

import pygame
from pygame.locals import *

import animation
import tilemap

sounds = {}
images = {}
animations = {}
tiles = {}
tilesets = {}

sound_defs = {
    "aoe" : "aoe.wav",
    "big hit" : "big_hit.wav",
    "burstfire" : "burstfire.wav",
    "explosion" : "explosion.wav",
    "fireball" : "fireball.wav", 
    "hover" : "heavy_hover.wav",
    "high pitch" : "high_pitch.wav",
    "jump" : "jump.wav",
    "long swing" : "longswing.wav",
    "pickaxe" : "pickaxe.wav",
    "pickup" : "pickup.wav",
    "select" : "select.wav",
    "short swing" : "shortswing.wav",
    "spell" : "spell.wav",
    "summon" : "summon.wav",
    "teleport" : "teleport.wav"
    }

# Not quite image defs, need an intermediate layer here
image_defs = {
    "resources/testsheet.png" : {
        "little dude" : (0, 0, 32, 32),
        "dark floor"  : (1, 0, 32, 32),
        "light floor" : (2, 0, 32, 32),
        "blue floor"  : (3, 0, 32, 32),
        "grass"       : (4, 0, 32, 32),
        },
    "resources/crackedfloor.png" : {
        "cracked floor" : (0, 0, 32, 32),
        },
    "resources/brickwall.png" : {
        "brick wall left"  : (0, 0, 32, 32),
        "brick wall mid"   : (1, 0, 32, 32),
        "brick wall right" : (2, 0, 32, 32),
        }    
    }

# Tiles = (image name, is_blocked)
tile_defs = {
    "dark floor"       : ("dark floor", False),
    "light floor"      : ("light floor", False),
    "blue floor"       : ("blue floor", False),
    "grass"            : ("grass", False),
    "cracked floor"    : ("cracked floor", False),
    "brick wall left"  : ("brick wall left", False),
    "brick wall mid"   : ("brick wall mid", False),
    "brick wall right" : ("brick wall right", False),
    }

tileset_defs = {
    "base_tileset" : [
        "dark floor",
        "light floor",
        "blue floor",
        "grass",
        "cracked floor",
        "brick wall mid",
        ],
    }


loaded_resources = False
def load_resources():
    """Fills the structure above with the resources for the game.
    """
    global loaded_resources
    if loaded_resources:
        return
    loaded_resources = True

    # Sounds
    for name, filename in sound_defs.iteritems():
        sounds[name] = pygame.mixer.Sound(filename)

    # Images
    for sheet_img, defs in image_defs.iteritems():
        img = pygame.image.load(sheet_img).convert_alpha()
        for name, (x, y, w, h, is_blocked) in defs.iteritems():
            x, y = x * w, y * h
            # Replace with an image object
            images[name] = tilemap.Tile(img, pygame.Rect(x, y, w, h), is_blocked)
        
    # Tiles
    for name, defs in tile_defs.iteritems():
        tiles[name] = [tilemap.Tile(images[img_name], for img_name,   in defs]
        
    # Tilesets
    for name, defs in tileset_defs.iteritems():
        tilesets[name] = [images[tile_name] for tile_name in defs]

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((10,10))
    load_resources()


        
