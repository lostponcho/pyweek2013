#!/usr/bin/env python

import os
import pygame
from pygame.locals import *
import pygame.joystick as gpad

import resourcemanager
import text
import tilemap
import camera
import animation
import entity

class Game(object):
    title = "Underworld Kerfuffle"
    width, height = 800, 600
    ticks_per_second = 30
    background_color = (60, 80, 60)

    def __init__(self, state):
        pygame.init()
        pygame.mixer.init()

        # pygame.key.set_repeat(300, 50)
        if not pygame.font:
            exit()

        # Detect and register gamepads
        self.gpads = []        
        if gpad.get_count() != 0:
            print "Gamepad(s) detected."
            count = gpad.get_count()
            for i in range(count):
                joy = gpad.Joystick(i)
                joy.init()
                print i, joy.get_name()
                self.gpads.append(joy)
            
        self.font_s = pygame.font.Font("resources/font/C64_Pro_Mono_v1.0-STYLE.ttf", 10)
        self.font_m = pygame.font.Font("resources/font/C64_Pro_Mono_v1.0-STYLE.ttf", 18)
        self.font_l = pygame.font.Font("resources/font/C64_Pro_Mono_v1.0-STYLE.ttf", 32)        
            
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width, self.height))
        
        resourcemanager.load_resources()
        
        pygame.display.set_caption(self.title)

        self.state = state(self)

        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill(self.background_color)

        self.screen.blit(self.background, (0, 0))
        self.state.display(self.screen)
        
    def run(self):
        while True:
            self.state.update(1/float(self.ticks_per_second))

            self.screen.blit(self.background, (0, 0))
            self.state.display(self.screen)

            pygame.display.flip()

            self.clock.tick(self.ticks_per_second)

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                else:
                    self.state.handle_event(event)

    def set_state(self, state):
        self.state = state

class TitleState(object):
    def __init__(self, game):
        self.game = game
        self.objs = []
        
        title = text.Text(x=0, y=40, font=game.font_l, text="Underworld Kerfuffle", color=(0, 0, 0))
        title.center_x(0, self.game.width)
        title.move(4, 4)
        self.objs.append(title)
        
        title = text.Text(x=0, y=40, font=game.font_l, text="Underworld Kerfuffle")
        title.center_x(0, self.game.width)
        self.objs.append(title)
        
        msg = text.Text(x=0, y=500, font=game.font_m, text="Press FIRE to start", color=(0, 0, 0))
        msg.center_x(0, self.game.width)
        msg.move(4, 4)
        self.objs.append(msg)
        
        msg = text.Text(x=0, y=500, font=game.font_m, text="Press FIRE to start", color=(100, 230, 230))
        msg.center_x(0, self.game.width)
        self.objs.append(msg)
        
    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                exit()
            elif event.key == K_SPACE:
                resourcemanager.sounds["select"].play()                
                self.game.set_state(GameState(self.game))
        elif event.type == pygame.JOYBUTTONDOWN:
            print "Joystick button {} pressed.".format(event.button)
            resourcemanager.sounds["select"].play()
            self.game.set_state(GameState(self.game))            
        elif event.type == pygame.JOYBUTTONUP:
            print "Joystick button {} released.".format(event.button)
        elif event.type == JOYBALLMOTION:
            print "JOYBALLMOTION"
        elif event.type == JOYHATMOTION:
            print "JOYHATMOTION"

    def update(self, tick):
        pass
            
    def display(self, screen):
        for obj in self.objs:
            obj.display(screen)

class GameState(object):
    def __init__(self, game):
        self.game = game
        
        self.x, self.y = 400, 300
        self.man = pygame.sprite.Sprite()
        self.man.image = resourcemanager.images["lich"]
        self.man.rect = self.man.image.rect.move(self.x, self.y)
        
        self.cx, self.cy = 400, 300
        self.cross = pygame.sprite.Sprite()
        self.cross.image = resourcemanager.images["crosshair"]        
        self.cross.rect = self.cross.image.rect.move(self.cx, self.cy)
        
        self.dx, self.dy = 0, 0
        self.cdx, self.cdy = 0, 0

        self.msg = text.Text(x=160, y=300, font=game.font_s, text="Avenge me!",
                             color=(0, 0, 0), background=(255, 255, 255), alpha=128)

        self.map = tilemap.TileMap(resourcemanager.tiles, "grass", 80, 60, 32, 32)
        self.map.random_fill(resourcemanager.tilesets["base_tileset"])
        self.map.add_edge_wall("brick wall mid")        

        self.camera = camera.Camera(self.game.width, self.game.height,
                                    self.map.w * self.map.tile_w,
                                    self.map.h * self.map.tile_h)

        self.entities = []

        self.entities.append(entity.make_small_explosion(self.game, pygame.Rect(80, 80, 0, 0)))
        
    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                resourcemanager.sounds["select"].play() 
                self.game.set_state(TitleState(self.game))
            elif event.key == K_w:
                self.dy -= 100
            elif event.key == K_a:
                self.dx -= 100
            elif event.key == K_s:
                self.dy += 100
            elif event.key == K_d:
                self.dx += 100
            elif event.key == K_p:
                resourcemanager.sounds["select"].play()
                self.game.set_state(PauseState(self.game, self))
            elif event.key == K_F12:
                for i in range(200):
                    filename = 'screenshot{}.png'.format(i)
                    if not os.path.isfile(filename):
                        pygame.image.save(self.game.screen, filename)
                        break
        elif event.type == KEYUP:
            if event.key == K_w:
                self.dy += 100
            elif event.key == K_a:
                self.dx += 100
            elif event.key == K_s:
                self.dy -= 100
            elif event.key == K_d:
                self.dx -= 100
        elif event.type == JOYAXISMOTION:
#            print "Movement on {} axis.".format(event.axis)
            if event.axis == 0:
                if abs(event.value) > 0.2:
                    self.dx = event.value * 100
                else:
                    self.dx = 0
            elif event.axis == 1:
                if abs(event.value) > 0.2:                    
                    self.dy = event.value * 100
                else:
                    self.dy = 0
            elif event.axis == 3:
                if abs(event.value) > 0.2:                                        
                    self.cdx = event.value * 100
                else:
                    self.cdx = 0
            elif event.axis == 4:
                if abs(event.value) > 0.2:                                                            
                    self.cdy = event.value * 100
                else:
                    self.cdy = 0
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 6:
                
            print "Joystick button {} pressed.".format(event.button)
            self.entities.append(entity.make_small_explosion(self.game,
                                                             Rect(self.man.rect.x, self.man.rect.y, 0, 0)))
            
        elif event.type == pygame.JOYBUTTONUP:
            print "Joystick button released."                
        elif event.type == JOYBALLMOTION:
            print "JOYBALLMOTION"
        elif event.type == JOYHATMOTION:
            print "JOYHATMOTION"

    def update(self, tick):
        dx, dy = self.map.collide(self.man.rect, self.dx * tick, self.dy * tick)
        self.man.rect.x += dx
        self.man.rect.y += dy

        self.camera.update(self.man.rect.x, self.man.rect.y)
        
        self.cross.rect.x += self.cdx * tick
        self.cross.rect.y += self.cdy * tick

        for entity in self.entities:
            entity.move_update()
            entity.animation_update()
            entity.ai_update()                        
        
        for i in xrange(len(self.entities) - 1, -1, -1):
            if self.entities[i].remove:
                del self.entities[i]
            
    def display(self, screen):
        self.map.display(screen, self.camera.pos)
        self.man.image.draw(screen, self.man.rect.move(-self.camera.pos.x, -self.camera.pos.y))
        self.cross.image.draw(screen, self.cross.rect.move(-self.camera.pos.x, -self.camera.pos.y))
        self.msg.display(screen)

        for entity in self.entities:
            entity.draw(screen, self.camera.pos)

class PauseState(object):
    def __init__(self, game, parent):
        self.game = game
        self.parent = parent
        self.img = self.game.screen.copy()
        self.text = text.Text(font=game.font_l, text="paused", color=(0, 0, 0), background=(255, 255, 255))
        self.text.center_x(0, self.game.width)
        self.text.center_y(0, self.game.height)

        # For debugging
        print "Entities:", ", ".join("<{}>".format(entity.name) for entity in self.parent.entities)
        
    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                resourcemanager.sounds["select"].play()                
                self.game.set_state(self.parent)

    def update(self, tick):
        pass
    
    def display(self, screen):
        screen.blit(self.img, (0, 0, self.game.width, self.game.height))
        self.text.display(screen)
        
if __name__ == '__main__':
    Game(TitleState).run()
