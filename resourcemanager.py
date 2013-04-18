# Manage resources here

import pygame
from pygame.locals import *

import os
import sys

import animation
import tilemap
import image

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
    "testsheet.png" : {
        "little dude" : (0, 0, 32, 32),
        "dark floor"  : (1, 0, 32, 32),
        "light floor" : (2, 0, 32, 32),
        "blue floor"  : (3, 0, 32, 32),
        "grass"       : (4, 0, 32, 32),
        },
    "crackedfloor.png" : {
        "cracked floor" : (0, 0, 32, 32),
        },
    "brickwall.png" : {
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
    "brick wall left"  : ("brick wall left", True),
    "brick wall mid"   : ("brick wall mid", True),
    "brick wall right" : ("brick wall right", True),
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

    if getattr(sys, 'frozen', None):
        basedir = sys._MEIPASS
    else:
        basedir = os.path.dirname(__file__)

    resourcedir = os.path.join(basedir, "resources")
    sounddir = os.path.join(resourcedir, "sound")
    imagedir = resourcedir
    
    # Sounds
    for name, filename in sound_defs.iteritems():
        print os.path.join(sounddir, filename)
        sounds[name] = pygame.mixer.Sound(os.path.join(sounddir, filename))

    # Images
    for filename, defs in image_defs.iteritems():
        img = pygame.image.load(os.path.join(imagedir, filename)).convert_alpha()
        for name, (x, y, w, h) in defs.iteritems():
            # Make it easier to specify above, by having x & y in units of w & h
            x, y = x * w, y * h
            # TODO: Replace with an image object
            images[name] = image.Image(img, pygame.Rect(x, y, w, h))
        
    # Tiles
    for name, (img_name, is_blocked) in tile_defs.iteritems():
        tiles[name] = tilemap.Tile(images[img_name], is_blocked)
        
    # Tilesets
    for name, defs in tileset_defs.iteritems():
        tilesets[name] = [tiles[tile_name] for tile_name in defs]

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((10,10))
    load_resources()


        
