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
    "castlefloor.png" : {
        "castle floor" : (0, 0, 32, 32),
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
    "castlewalls.png" : {
        "castle wall 1011" : (0, 0, 32, 32),
        "castle wall 1010" : (1, 0, 32, 32),
        "castle wall 1110" : (2, 0, 32, 32),
        "castle wall 0000" : (3, 0, 32, 32),
        "castle wall 1111" : (0, 1, 32, 32),
        "castle wall 0111" : (1, 1, 32, 32),
        "castle wall 1101" : (2, 1, 32, 32),
        "castle wall 0101" : (3, 1, 32, 32),
        "castle wall 1001" : (0, 2, 32, 32),
        "castle wall 1000" : (1, 2, 32, 32),
        "castle wall 1100" : (2, 2, 32, 32),
        "castle wall 0100" : (3, 2, 32, 32),
        "castle wall 0011" : (0, 3, 32, 32),
        "castle wall 0010" : (1, 3, 32, 32),
        "castle wall 0110" : (2, 3, 32, 32),
        "castle wall 0001" : (3, 3, 32, 32),
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

    "peasant.png" : {
        "peasant down fire" : (0, 0, 32, 32),
        "peasant down 0" : (1, 0, 32, 32),
        "peasant down 1" : (2, 0, 32, 32),
        "peasant down 2" : (3, 0, 32, 32),
        "peasant up fire" : (0, 1, 32, 32),
        "peasant up 0" : (1, 1, 32, 32),
        "peasant up 1" : (2, 1, 32, 32),
        "peasant up 2" : (3, 1, 32, 32),
        "peasant right fire" : (0, 2, 32, 32),
        "peasant right 0" : (1, 2, 32, 32),
        "peasant right 1" : (2, 2, 32, 32),
        "peasant right 2" : (3, 2, 32, 32),
        "peasant left fire" : (0, 3, 32, 32),
        "peasant left 0" : (1, 3, 32, 32),
        "peasant left 1" : (2, 3, 32, 32),
        "peasant left 2" : (3, 3, 32, 32),
        },
    "imp.png" : {
        "imp down fire" : (0, 0, 32, 32),
        "imp down 0" : (1, 0, 32, 32),
        "imp down 1" : (2, 0, 32, 32),
        "imp down 2" : (3, 0, 32, 32),
        "imp up fire" : (0, 1, 32, 32),
        "imp up 0" : (1, 1, 32, 32),
        "imp up 1" : (2, 1, 32, 32),
        "imp up 2" : (3, 1, 32, 32),
        "imp right fire" : (0, 2, 32, 32),
        "imp right 0" : (1, 2, 32, 32),
        "imp right 1" : (2, 2, 32, 32),
        "imp right 2" : (3, 2, 32, 32),
        "imp left fire" : (0, 3, 32, 32),
        "imp left 0" : (1, 3, 32, 32),
        "imp left 1" : (2, 3, 32, 32),
        "imp left 2" : (3, 3, 32, 32),
        },
    "knight.png" : {
        "knight down fire"  : (0, 0, 32, 37),
        "knight down 0"     : (1, 0, 32, 37),
        "knight down 1"     : (2, 0, 32, 37),
        "knight down 2"     : (3, 0, 32, 37),
        "knight up fire"    : (0, 1, 32, 37),
        "knight up 0"       : (1, 1, 32, 37),
        "knight up 1"       : (2, 1, 32, 37),
        "knight up 2"       : (3, 1, 32, 37),
        "knight right fire" : (0, 2, 32, 37),
        "knight right 0"    : (1, 2, 32, 37),
        "knight right 1"    : (2, 2, 32, 37),
        "knight right 2"    : (3, 2, 32, 37),
        "knight left fire"  : (0, 3, 32, 37),
        "knight left 0"     : (1, 3, 32, 37),
        "knight left 1"     : (2, 3, 32, 37),
        "knight left 2"     : (3, 3, 32, 37),
        },
    "fireball.png" : {
        "fireball right 0"    : (0, 0, 16, 16),
        "fireball right 1"    : (1, 0, 16, 16),         
        "fireball left 0"     : (2, 0, 16, 16),
        "fireball left 1"     : (3, 0, 16, 16),         
        "fireball down 0"     : (0, 1, 16, 16),
        "fireball down 1"     : (1, 1, 16, 16),         
        "fireball up 0"       : (2, 1, 16, 16),
        "fireball up 1"       : (3, 1, 16, 16),         
        "fireball down left"  : (0, 2, 16, 16),
        "fireball down right" : (1, 2, 16, 16),         
        "fireball up right"   : (2, 2, 16, 16),
        "fireball up left"    : (3, 2, 16, 16),
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
        "lich down fire", "lich down fire", "lich down fire", "lich down fire",
        ],
    "lich down" : [
        "lich down 0",
        "lich down 1",
        "lich down 2",
        ],
    "lich up fire" : [
        "lich up fire", "lich up fire", "lich up fire", "lich up fire",
        ],
    "lich up" : [
        "lich up 0",
        ],
    "lich right fire" : [
        "lich right fire", "lich right fire", "lich right fire", "lich right fire",
        ],
    "lich right" : [
        "lich right 0",
        ],
    "lich left fire" : [
        "lich left fire", "lich left fire", "lich left fire", "lich left fire",
        ],
    "lich left" : [
        "lich left 0",
        ],


    ### PEASANT ###
    "peasant down fire" : [
        "peasant down fire", "peasant down fire", "peasant down fire", "peasant down fire",
        ],
    "peasant down" : [
        "peasant down 0",
        "peasant down 1",
        "peasant down 2",
        ],
    "peasant up fire" : [
        "peasant up fire", "peasant up fire", "peasant up fire", "peasant up fire",
        ],
    "peasant up" : [
        "peasant up 0",
        "peasant up 1",
        "peasant up 2",        
        ],
    "peasant right fire" : [
        "peasant right fire", "peasant right fire", "peasant right fire", "peasant right fire",
        ],
    "peasant right" : [
        "peasant right 0",
        "peasant right 1",
        "peasant right 2",
        ],
    "peasant left fire" : [
        "peasant left fire", "peasant left fire", "peasant left fire", "peasant left fire",
        ],
    "peasant left" : [
        "peasant left 0",
        "peasant left 1",
        "peasant left 2",        
        ],
    
    ### IMP ###
    "imp down fire" : [
        "imp down fire", "imp down fire", "imp down fire", "imp down fire",
        ],
    "imp down" : [
        "imp down 0",
        "imp down 1",
        "imp down 2",
        ],
    "imp up fire" : [
        "imp up fire", "imp up fire", "imp up fire", "imp up fire",
        ],
    "imp up" : [
        "imp up 0",
        "imp up 1",
        "imp up 2",        
        ],
    "imp right fire" : [
        "imp right fire", "imp right fire", "imp right fire", "imp right fire",
        ],
    "imp right" : [
        "imp right 0",
        "imp right 1",
        "imp right 2",
        ],
    "imp left fire" : [
        "imp left fire", "imp left fire", "imp left fire", "imp left fire",
        ],
    "imp left" : [
        "imp left 0",
        "imp left 1",
        "imp left 2",        
        ],

    ### KNIGHT ###
    "knight down fire" : [
        "knight down fire", "knight down fire", "knight down fire", "knight down fire",
        ],
    "knight down" : [
        "knight down 0",
        "knight down 1",
        "knight down 2",
        ],
    "knight up fire" : [
        "knight up fire", "knight up fire", "knight up fire", "knight up fire",
        ],
    "knight up" : [
        "knight up 0",
        "knight up 1",
        "knight up 2",        
        ],
    "knight right fire" : [
        "knight right fire", "knight right fire", "knight right fire", "knight right fire",
        ],
    "knight right" : [
        "knight right 0",
        "knight right 1",
        "knight right 2",
        ],
    "knight left fire" : [
        "knight left fire", "knight left fire", "knight left fire", "knight left fire",
        ],
    "knight left" : [
        "knight left 0",
        "knight left 1",
        "knight left 2",        
        ],

    "fireball right" : [
        "fireball right 0",
        "fireball right 1",
        ],
    "fireball left" : [
        "fireball left 0",
        "fireball left 1",
        ],
    "fireball down" : [
        "fireball down 0",
        "fireball down 1",
        ],
    "fireball up" : [
        "fireball up 0",
        "fireball up 1",
        ],
    "fireball down right" : [
        "fireball down right",
        ],
    "fireball down left" : [
        "fireball down left",
        ],
    "fireball up right" : [
        "fireball up right",
        ],
    "fireball up left" : [
        "fireball up left",
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

    "peasant down fire" : ("peasant down fire", "peasant down"),
    "peasant down" : ("peasant down", "peasant down"),
    "peasant up fire" : ("peasant up fire", "peasant up"),
    "peasant up" : ("peasant up", "peasant up"),
    "peasant right fire" : ("peasant right fire", "peasant right"),
    "peasant right" : ("peasant right", "peasant right"),
    "peasant left fire" : ("peasant left fire", "peasant left"),
    "peasant left" : ("peasant left", "peasant left"),

    "imp down fire" : ("imp down fire", "imp down"),
    "imp down" : ("imp down", "imp down"),
    "imp up fire" : ("imp up fire", "imp up"),
    "imp up" : ("imp up", "imp up"),
    "imp right fire" : ("imp right fire", "imp right"),
    "imp right" : ("imp right", "imp right"),
    "imp left fire" : ("imp left fire", "imp left"),
    "imp left" : ("imp left", "imp left"),

    "knight down fire" : ("knight down fire", "knight down"),
    "knight down" : ("knight down", "knight down"),
    "knight up fire" : ("knight up fire", "knight up"),
    "knight up" : ("knight up", "knight up"),
    "knight right fire" : ("knight right fire", "knight right"),
    "knight right" : ("knight right", "knight right"),
    "knight left fire" : ("knight left fire", "knight left"),
    "knight left" : ("knight left", "knight left"),

    "fireball right" : ("fireball right", "fireball right"), 
    "fireball left" : ("fireball left", "fireball left"), 
    "fireball up" : ("fireball up", "fireball up"), 
    "fireball down" : ("fireball down", "fireball down"), 
    "fireball down right" : ("fireball down right", "fireball down right"), 
    "fireball up right" : ("fireball up right", "fireball up right"), 
    "fireball down left" : ("fireball down left", "fireball down left"), 
    "fireball up left" : ("fireball up left", "fireball up left"), 
    }

# Tiles = (image name, is_blocked)
tile_defs = {
    "dark floor"       : ("dark floor", False),
    "light floor"      : ("light floor", False),
    "blue floor"       : ("blue floor", False),
    "grass"            : ("grass", False),
    "cracked floor"    : ("cracked floor", False),
    "castle floor"     : ("castle floor", False),    
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

    "castle wall 1011"  : ("castle wall 1011", True),
    "castle wall 1010"  : ("castle wall 1010", True),
    "castle wall 1110"  : ("castle wall 1110", True),
    "castle wall 0000"  : ("castle wall 0000", True),
    "castle wall 1111"  : ("castle wall 1111", True),
    "castle wall 0111"  : ("castle wall 0111", True),
    "castle wall 1101"  : ("castle wall 1101", True),
    "castle wall 0101"  : ("castle wall 0101", True),
    "castle wall 1001"  : ("castle wall 1001", True),
    "castle wall 1000"  : ("castle wall 1000", True),
    "castle wall 1100"  : ("castle wall 1100", True),
    "castle wall 0100"  : ("castle wall 0100", True),
    "castle wall 0011"  : ("castle wall 0011", True),
    "castle wall 0010"  : ("castle wall 0010", True),
    "castle wall 0110"  : ("castle wall 0110", True),
    "castle wall 0001"  : ("castle wall 0001", True),
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
    "generation" : [
        "dark floor", "dark floor", "dark floor", "dark floor", "dark floor",
        "light floor", "light floor", "light floor", "light floor", "light floor",
        "blue floor", "blue floor", "blue floor", "blue floor", "blue floor",
        "blue floor", "blue floor", "blue floor", "blue floor", "blue floor",
        "brick wall 0000",        
        ],
    "base floors" : [
        "dark floor",
        "light floor",
        "blue floor",
        ],
    "evil floors" : [
        "dark floor",
        "cracked floor",
        ],
    "good floors" : [
        "light floor",
        "grass",
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
    "castle_tiles" : [
        "castle wall 0000",
        "castle wall 0001",
        "castle wall 0010",
        "castle wall 0011",
        "castle wall 0100",
        "castle wall 0101",        
        "castle wall 0110",
        "castle wall 0111",
        "castle wall 1000",
        "castle wall 1001",
        "castle wall 1010",
        "castle wall 1011",
        "castle wall 1100",
        "castle wall 1101",
        "castle wall 1110",
        "castle wall 1111",
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
        # try:
        #     # Pyinstaller
        #     basedir = sys._MEIPASS
        # except:
        #     # Py2exe
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
