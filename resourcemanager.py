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
animation_lists = {}
animation_states = {}
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
    "skeletonmage.png" : {"lich" : (0, 0, 31, 31),},
    "man.png" : {"man" : (0, 0, 36, 36),},
    "crosshair.png" : {"crosshair" : (0, 0, 36, 36),},        
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
        },
    "explosion27.png" : {
        "explosion small 1" : (1, 0, 64, 64),
        "explosion small 2" : (2, 0, 64, 64),
        "explosion small 3" : (3, 0, 64, 64),
        "explosion small 4" : (0, 1, 64, 64),
        "explosion small 5" : (1, 1, 64, 64),
        "explosion small 6" : (2, 1, 64, 64),
        "explosion small 7" : (3, 1, 64, 64),        
        "explosion small 8" : (0, 2, 64, 64),
        "explosion small 9" : (1, 2, 64, 64),
        "explosion small 10" : (2, 2, 64, 64),
        "explosion small 11" : (3, 2, 64, 64),
        "explosion small 12" : (0, 3, 64, 64),
        "explosion small 13" : (1, 3, 64, 64),
        "explosion small 14" : (2, 3, 64, 64),
        },
    "explosion31.png" : {
        "explosion medium 1" : (1, 0, 64, 64),
        "explosion medium 2" : (2, 0, 64, 64),
        "explosion medium 3" : (3, 0, 64, 64),
        "explosion medium 4" : (0, 1, 64, 64),
        "explosion medium 5" : (1, 1, 64, 64),
        "explosion medium 6" : (2, 1, 64, 64),
        "explosion medium 7" : (3, 1, 64, 64),        
        "explosion medium 8" : (0, 2, 64, 64),
        "explosion medium 9" : (1, 2, 64, 64),
        "explosion medium 10" : (2, 2, 64, 64),
        "explosion medium 11" : (3, 2, 64, 64),
        "explosion medium 12" : (0, 3, 64, 64),
        "explosion medium 13" : (1, 3, 64, 64),
        "explosion medium 14" : (2, 3, 64, 64),
        },
    "explosion33.png" : {
        "explosion large 1" : (1, 0, 64, 64),
        "explosion large 2" : (2, 0, 64, 64),
        "explosion large 3" : (3, 0, 64, 64),
        "explosion large 4" : (0, 1, 64, 64),
        "explosion large 5" : (1, 1, 64, 64),
        "explosion large 6" : (2, 1, 64, 64),
        "explosion large 7" : (3, 1, 64, 64),        
        "explosion large 8" : (0, 2, 64, 64),
        "explosion large 9" : (1, 2, 64, 64),
        "explosion large 10" : (2, 2, 64, 64),
        "explosion large 11" : (3, 2, 64, 64),
        "explosion large 12" : (0, 3, 64, 64),
        "explosion large 13" : (1, 3, 64, 64),
        "explosion large 14" : (2, 3, 64, 64),
        },
    }

# Animations are broken up into some parts
# First the basic lists of images
animation_list_defs = {
    "explosion small" : [
        "explosion small 1",
        "explosion small 2",
        "explosion small 3",
        "explosion small 4",
        "explosion small 5",
        "explosion small 6",
        "explosion small 7",
        "explosion small 8",
        "explosion small 9",
        "explosion small 10",
        "explosion small 11",
        "explosion small 12",
        "explosion small 13",
        "explosion small 14",
        ],
    "explosion medium" : [
        "explosion medium 1",
        "explosion medium 2",
        "explosion medium 3",
        "explosion medium 4",
        "explosion medium 5",
        "explosion medium 6",
        "explosion medium 7",
        "explosion medium 8",
        "explosion medium 9",
        "explosion medium 10",
        "explosion medium 11",
        "explosion medium 12",
        "explosion medium 13",
        "explosion medium 14",
        ],
    "explosion large" : [
        "explosion large 1",
        "explosion large 2",
        "explosion large 3",
        "explosion large 4",
        "explosion large 5",
        "explosion large 6",
        "explosion large 7",
        "explosion large 8",
        "explosion large 9",
        "explosion large 10",
        "explosion large 11",
        "explosion large 12",
        "explosion large 13",
        "explosion large 14",
        ],
    }

# Second the state definitions (a list reference, and a next state)
animation_state_defs = {
    "small explosion" : ("explosion small", None),
    "medium explosion" : ("explosion medium", None),
    "large explosion" : ("explosion large", None),    
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
        sounds[name] = pygame.mixer.Sound(os.path.join(sounddir, filename))

    # Images
    for filename, defs in image_defs.iteritems():
        img = pygame.image.load(os.path.join(imagedir, filename)).convert_alpha()
        for name, (x, y, w, h) in defs.iteritems():
            # Make it easier to specify above, by having x & y in units of w & h
            x, y = x * w, y * h
            # TODO: Replace with an image object
            images[name] = image.Image(img, pygame.Rect(x, y, w, h))

    # Animations
    for name, img_list in animation_list_defs.iteritems():
        animation_lists[name] = [images[img_name] for img_name in img_list]

    # Animations
    for name, (list_name, next_state) in animation_state_defs.iteritems():
        animation_states[name] = animation.Animation_State(animation_lists[list_name], next_state)

    # Fix up for animation_states (So we can handle recursive animation_state transitions)
    for animation_state in animation_states.itervalues():
        if animation_state.next_state is not None:
            animation_state.next_state = animation_states[animation_state.next_state]

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
