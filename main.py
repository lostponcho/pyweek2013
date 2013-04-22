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
import random
import world

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

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.width, self.height))

        resourcemanager.load_resources()

        self.font_s = pygame.font.Font(resourcemanager.fontpath, 10)
        self.font_m = pygame.font.Font(resourcemanager.fontpath, 18)
        self.font_l = pygame.font.Font(resourcemanager.fontpath, 32)

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

# TODO: Not ready yet
#        self.world = world.make_default_world()
        
        self.entities = []

        player = entity.make_lich(self, 5 * 32, 35 * 32)
        self.entities.append(player)
        self.player = entity.Player(self, player)
        self.player_speed = 150

        self.cdx, self.cdy = 0, 0
        self.cross = pygame.sprite.Sprite()
        self.cross.image = resourcemanager.images["crosshair"]
        self.cross.rect = self.cross.image.rect.move(self.game.width / 2, self.game.height / 2)

        self.hud = text.Text(x=10, y=10, font=game.font_s, text="HUD MESSAGE!",
                             color=(255, 255, 255), background=(0, 0, 255), alpha=96)

#        floors, evil floors, good floors
        self.map = tilemap.TileMap(resourcemanager.tiles, "grass", 80, 60, 32, 32)
        self.map.random_fill(resourcemanager.tilesets["generation"])
        self.map.add_circle(60, 10, 10, "grass")
        self.map.add_circle(50, 20, 10, "grass")
        self.map.add_circle(70, 20, 10, "grass")
        self.map.add_filled_box(60, 0, 20, 20, "castle floor")
        self.map.add_circle(10, 45, 10, "dark floor")
        self.map.add_circle(10, 45, 5, "cracked floor")
        self.map.add_circle(5, 35, 5, "cracked floor")
        self.map.add_line(60, 59, 40, 30, "brick wall 0000")
        self.map.add_line(61, 59, 41, 30, "brick wall 0000")
        self.map.add_line(0, 20, 30, 50, "brick wall 0000")
        self.map.add_line(1, 20, 31, 50, "brick wall 0000")
        self.map.add_edge_wall("brick wall 0000")
        self.map.add_line(60, 10, 70, 10, "castle wall 0000")
        self.map.add_box(60, 0, 20, 20, "castle wall 0000")
        self.map.add_filled_box(60, 17, 3, 3, "castle floor")
        self.map.fix_brick_walls()

        self.entities.append(entity.make_knight(self, 32 * 62, 32 * 5))
        for _ in range(5):
            self.entities.append(entity.make_peasant(self, 32 * 60, 32 * 25))
        for _ in range(5):
            self.entities.append(entity.make_peasant(self, 32 * 50, 32 * 20))
        for _ in range(5):
            self.entities.append(entity.make_peasant(self, 32 * 50, 32 * 10))

        for i in range(4):
            self.entities.append(entity.make_imp(self, 32 * (10 + i), 32 * 45))
            
        self.camera = camera.Camera(self.game.width, self.game.height,
                                    self.map.w * self.map.tile_w,
                                    self.map.h * self.map.tile_h)


    # TODO: send messages to a controls object that can change bindings
    def handle_event(self, event):
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                resourcemanager.sounds["select"].play()
                self.game.set_state(TitleState(self.game))
            elif event.key == K_w:
                self.player.dy -= self.player_speed
            elif event.key == K_a:
                self.player.dx -= self.player_speed
            elif event.key == K_s:
                self.player.dy += self.player_speed
            elif event.key == K_d:
                self.player.dx += self.player_speed
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
                self.player.dy += self.player_speed
            elif event.key == K_a:
                self.player.dx += self.player_speed
            elif event.key == K_s:
                self.player.dy -= self.player_speed
            elif event.key == K_d:
                self.player.dx -= self.player_speed
        elif event.type == JOYAXISMOTION:
            if event.axis == 0:
                if abs(event.value) > 0.2:
                    self.player.dx = event.value * self.player_speed
                else:
                    self.player.dx = 0
            elif event.axis == 1:
                if abs(event.value) > 0.2:
                    self.player.dy = event.value * self.player_speed
                else:
                    self.player.dy = 0
            elif event.axis == 3:
                if abs(event.value) > 0.2:
                    self.cdx = event.value * 300
                else:
                    self.cdx = 0
            elif event.axis == 4:
                if abs(event.value) > 0.2:
                    self.cdy = event.value * 300
                else:
                    self.cdy = 0
            else:
                print "Movement on {} axis.".format(event.axis)
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 5:
                select = random.randint(0,3)
                if select == 0:
                    self.entities.append(entity.make_spider(self,
                                                            self.player.entity.pos.x,
                                                            self.player.entity.pos.y))

                elif select == 1:
                    self.entities.append(entity.make_knight(self,
                                                            self.player.entity.pos.x,
                                                            self.player.entity.pos.y))
                elif select == 2:
                    self.entities.append(entity.make_peasant(self,
                                                            self.player.entity.pos.x,
                                                            self.player.entity.pos.y))
                else:
                    self.entities.append(entity.make_imp(self,
                                                            self.player.entity.pos.x,
                                                            self.player.entity.pos.y))
            elif event.button == 6:
                resourcemanager.sounds["select"].play()
                self.game.set_state(PauseState(self.game, self))
            else:
                tx = self.camera.pos.x + self.cross.rect.x - self.player.entity.pos.x
                ty = self.camera.pos.y + self.cross.rect.y - self.player.entity.pos.y
                if tx == 0 and ty == 0: tx = 1
                
                self.entities.append(entity.make_fireball(self,
                                                          self.player.entity.pos.x,
                                                          self.player.entity.pos.y,
                                                          tx, ty))
        elif event.type == pygame.JOYBUTTONUP:
            print "Joystick button released."
        elif event.type == JOYBALLMOTION:
            print "JOYBALLMOTION"
        elif event.type == JOYHATMOTION:
            print "JOYHATMOTION"

    def update(self, tick):
        self.camera.update(self.player.entity.pos.x, self.player.entity.pos.y)

        self.cross.rect.x += self.cdx * tick
        self.cross.rect.y += self.cdy * tick

        for entity in self.entities:
            entity.ai_update()
            entity.move_update(tick)
            entity.animation_update()


        for i in xrange(len(self.entities) - 1, -1, -1):
            if self.entities[i].remove:
                del self.entities[i]

    def display(self, screen):
        self.map.display(screen, self.camera.pos)

        self.cross.image.draw(screen, self.cross.rect)

        for entity in self.entities:
            entity.draw(screen, self.camera.pos)

        self.hud.display(screen)

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
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 6:
                resourcemanager.sounds["select"].play()
                self.game.set_state(self.parent)

    def update(self, tick):
        pass

    def display(self, screen):
        screen.blit(self.img, (0, 0, self.game.width, self.game.height))
        self.text.display(screen)

if __name__ == '__main__':
    Game(TitleState).run()
