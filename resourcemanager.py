# Manage resources here

import pygame
from pygame.locals import *

import animation

sounds = {}
images = {}
animations = {}

loaded_resources = False


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

def load_resources():
    """Fills the structure above with the resources for the game.
    """
    if loaded_resources:
        return
    loaded_resources = True

    for name, filename in sound_defs.iteritems():
        sounds[name] = pygame.mixer.Sound(filename)
    
