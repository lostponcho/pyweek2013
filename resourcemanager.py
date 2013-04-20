# Manage resources here

import pygame
from pygame.locals import *

import os
import sys

import animation
import tilemap
import image

fontpath = None

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
        "brick wall 1011" : (0, 0, 32, 32),
        "brick wall 1010" : (1, 0, 32, 32),
        "brick wall 1110" : (2, 0, 32, 32),
        "brick wall 0000" : (3, 0, 32, 32),
        "brick wall 1111" : (0, 1, 32, 32),
        "brick wall 0111" : (1, 1, 32, 32),
        "brick wall 1101" : (2, 1, 32, 32),
        "brick wall 0101" : (3, 1, 32, 32),
        "brick wall 1001" : (0, 2, 32, 32),
        "brick wall 1000" : (1, 2, 32, 32),
        "brick wall 1100" : (2, 2, 32, 32),
        "brick wall 0100" : (3, 2, 32, 32),
        "brick wall 0011" : (0, 3, 32, 32),
        "brick wall 0010" : (1, 3, 32, 32),
        "brick wall 0110" : (2, 3, 32, 32),
        "brick wall 0001" : (3, 3, 32, 32),
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
    "4legged.png" : {
        "spider down 0" : (0, 0, 32, 32),
        "spider down 1" : (1, 0, 32, 32),
        "spider down 2" : (2, 0, 32, 32),
        "spider down 3" : (3, 0, 32, 32),
        "spider up 0" : (0, 1, 32, 32),
        "spider up 1" : (1, 1, 32, 32),
        "spider up 2" : (2, 1, 32, 32),
        "spider up 3" : (3, 1, 32, 32),
        "spider right 0" : (0, 2, 32, 32),
        "spider right 1" : (1, 2, 32, 32),
        "spider right 2" : (2, 2, 32, 32),
        "spider right 3" : (3, 2, 32, 32),
        "spider left 0" : (0, 3, 32, 32),
        "spider left 1" : (1, 3, 32, 32),
        "spider left 2" : (2, 3, 32, 32),
        "spider left 3" : (3, 3, 32, 32),
        },
    "skeletonmage.png" : {
        "lich down fire" : (0, 0, 32, 32),
        "lich down 0" : (1, 0, 32, 32),
        "lich down 1" : (2, 0, 32, 32),
        "lich down 2" : (3, 0, 32, 32),
        "lich up fire" : (1, 0, 32, 32),
        "lich up 0" : (1, 1, 32, 32),
        "lich right fire" : (2, 0, 32, 32),
        "lich right 0" : (2, 1, 32, 32),
        "lich left fire" : (2, 2, 32, 32),
        "lich left 0" : (2, 3, 32, 32),
        },
    }

# Animations are broken up into some parts
# First the basic lists of images
animation_list_defs = {
    ### EXPLOSIONS ###
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

    ### SPIDER ###    
    "spider up" : [
        "spider up 0",
        "spider up 1",
        "spider up 2",
        "spider up 3",
        ],
    "spider down" : [
        "spider down 0",
        "spider down 1",
        "spider down 2",
        "spider down 3",
        ],
    "spider right" : [
        "spider right 0",
        "spider right 1",
        "spider right 2",
        "spider right 3",
        ],
    "spider left" : [
        "spider left 0",
        "spider left 1",
        "spider left 2",
        "spider left 3",
        ],

    ### LICH ###
    "lich down fire" : [
        "lich down fire",
        "lich down fire",
        "lich down fire",
        "lich down fire",
        ],
    "lich down" : [
        "lich down 0",
        "lich down 1",
        "lich down 2",
        ],
    "lich up fire" : [
        "lich up fire",
        "lich up fire",
        "lich up fire",
        "lich up fire",
        ],
    "lich up" : [
        "lich up 0",
        ],
    "lich right fire" : [
        "lich right fire",
        "lich right fire",
        "lich right fire",
        "lich right fire",
        ],
    "lich right" : [
        "lich right 0",
        ],
    "lich left fire" : [
        "lich left fire",
        "lich left fire",
        "lich left fire",
        "lich left fire",
        ],
    "lich left" : [
        "lich left 0",
        ],
    }

# Second the state definitions (a list reference, and a next state)
animation_state_defs = {
    "small explosion" : ("explosion small", None),
    "medium explosion" : ("explosion medium", None),
    "large explosion" : ("explosion large", None),
    "spider up" : ("spider up", "spider up"),
    "spider down" : ("spider down", "spider down"),
    "spider right" : ("spider right", "spider right"),
    "spider left" : ("spider left", "spider left"),

    "lich down fire" : ("lich down fire", "lich down"),
    "lich down" : ("lich down", "lich down"),
    "lich up fire" : ("lich up fire", "lich up"),
    "lich up" : ("lich up", "lich up"),
    "lich right fire" : ("lich right fire", "lich right"),
    "lich right" : ("lich right", "lich right"),
    "lich left fire" : ("lich left fire", "lich left"),
    "lich left" : ("lich left", "lich left"),
    }

# Tiles = (image name, is_blocked)
tile_defs = {
    "dark floor"       : ("dark floor", False),
    "light floor"      : ("light floor", False),
    "blue floor"       : ("blue floor", False),
    "grass"            : ("grass", False),
    "cracked floor"    : ("cracked floor", False),
    "brick wall 1011"  : ("brick wall 1011", True),
    "brick wall 1010"  : ("brick wall 1010", True),
    "brick wall 1110"  : ("brick wall 1110", True),
    "brick wall 0000"  : ("brick wall 0000", True),
    "brick wall 1111"  : ("brick wall 1111", True),
    "brick wall 0111"  : ("brick wall 0111", True),
    "brick wall 1101"  : ("brick wall 1101", True),
    "brick wall 0101"  : ("brick wall 0101", True),
    "brick wall 1001"  : ("brick wall 1001", True),
    "brick wall 1000"  : ("brick wall 1000", True),
    "brick wall 1100"  : ("brick wall 1100", True),
    "brick wall 0100"  : ("brick wall 0100", True),
    "brick wall 0011"  : ("brick wall 0011", True),
    "brick wall 0010"  : ("brick wall 0010", True),
    "brick wall 0110"  : ("brick wall 0110", True),
    "brick wall 0001"  : ("brick wall 0001", True),
    }

tileset_defs = {
    "base_tileset" : [
        "dark floor",
        "light floor",
        "blue floor",
        "grass",
        "cracked floor",
        "brick wall 0000",
        ],
    "brick_tiles" : [
        "brick wall 0000",
        "brick wall 0001",
        "brick wall 0010",
        "brick wall 0011",
        "brick wall 0100",
        "brick wall 0101",        
        "brick wall 0110",
        "brick wall 0111",
        "brick wall 1000",
        "brick wall 1001",
        "brick wall 1010",
        "brick wall 1011",
        "brick wall 1100",
        "brick wall 1101",
        "brick wall 1110",
        "brick wall 1111",
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
        try:
            # Pyinstaller
            basedir = sys._MEIPASS
        except:
            # Py2exe
            basedir = '.'
    else:
        basedir = os.path.dirname(__file__)

    resourcedir = os.path.join(basedir, "resources")
    sounddir = os.path.join(resourcedir, "sound")
    imagedir = resourcedir
    fontdir = os.path.join(resourcedir, "font")
    global fontpath
    fontpath = os.path.join(fontdir, "C64_Pro_Mono_v1.0-STYLE.ttf")
    
    # Sounds
    for name, filename in sound_defs.iteritems():
        sounds[name] = pygame.mixer.Sound(os.path.join(sounddir, filename))

    # Images
    for filename, defs in image_defs.iteritems():
        img = pygame.image.load(os.path.join(imagedir, filename)).convert_alpha()
        for name, (x, y, w, h) in defs.iteritems():
            # Make it easier to specify above, by having x & y in units of w & h
            x, y = x * w, y * h
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
