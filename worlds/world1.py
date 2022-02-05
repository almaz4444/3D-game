from ursina import *
import sys
from block import *
sys.path.append('../Parkour/')

normalSpeed = 2
boostSpeed  = 5 
normalJump = 0.3

class World1(Entity):
    def __init__(self):
        super().__init__()

        self.menu = Entity(parent = self, enabled = True)
        self.is_enabled = True
        self.player = None

        self.grass1 = GrassBlock((-6, -17, 3))

        self.door1 = Door((11.1, -9, -10))
        self.door2 = Door((10.8, -10, 10.8), scale=(9.6, 9, 8))
        self.home = Home((10, -10, 0))
        self.sun = Sun((500, 500, 500))

        self.open = False

    def disable(self):
        self.is_enabled = False

        self.grass1.disable()

        self.door1.disable()
        self.door2.disable()
    
    def enable(self):
        self.is_enabled = True

        self.grass1.enable()

        self.door1.enable()
        self.door2.enable()

    def speed(self):
        self.player.SPEED = normalSpeed

    def update(self):
        print(round(camera.world_position.x), round(camera.world_position.z))
        if (round(camera.world_position.x), round(camera.world_position.z)) == (10, -11) or \
            (round(camera.world_position.x), round(camera.world_position.z)) == (10, -10) or \
                (round(camera.world_position.x), round(camera.world_position.z)) == (10, -9) or \
                    (round(camera.world_position.x), round(camera.world_position.z)) == (12, -7) or \
                        (round(camera.world_position.x), round(camera.world_position.z)) == (10, -8) or \
                            (round(camera.world_position.x), round(camera.world_position.z)) == (10, -7) or \
                                (round(camera.world_position.x), round(camera.world_position.z)) == (11, -7) or \
                                    (round(camera.world_position.x), round(camera.world_position.z)) == (11, -8) or \
                                        (round(camera.world_position.x), round(camera.world_position.z)) == (11, -9) or \
                                            (round(camera.world_position.x), round(camera.world_position.z)) == (12, -8) or \
                                                (round(camera.world_position.x), round(camera.world_position.z)) == (12, -9):
                                                    if self.door1.rotation_y >= 90:
                                                        self.door1.rotation_y -= held_keys['e'] * time.dt * 50
                                                        self.open = True
                                                    elif self.door1.rotation_y <= 0:
                                                        self.door1.rotation_y += held_keys['e'] * time.dt * 50
                                                        self.open = False
                                                    else:
                                                        if self.open == True:
                                                            self.door1.rotation_y -= held_keys['e'] * time.dt * 50
                                                        else:
                                                            self.door1.rotation_y += held_keys['e'] * time.dt * 50

        if (round(camera.world_position.x), round(camera.world_position.z)) == (9, 12) or\
            (round(camera.world_position.x), round(camera.world_position.z)) == (10, 12) or\
                (round(camera.world_position.x), round(camera.world_position.z)) == (10, 13) or\
                    (round(camera.world_position.x), round(camera.world_position.z)) == (11, 12) or\
                        (round(camera.world_position.x), round(camera.world_position.z)) == (8, 11) or\
                            (round(camera.world_position.x), round(camera.world_position.z)) == (9, 11) or\
                                (round(camera.world_position.x), round(camera.world_position.z)) == (9, 9) or\
                                    (round(camera.world_position.x), round(camera.world_position.z)) == (9, 10) or\
                                        (round(camera.world_position.x), round(camera.world_position.z)) == (8, 10) or\
                                            (round(camera.world_position.x), round(camera.world_position.z)) == (10, 10) or\
                                                (round(camera.world_position.x), round(camera.world_position.z)) == (10, 11) or\
                                                    (round(camera.world_position.x), round(camera.world_position.z)) == (11, 10) or\
                                                        (round(camera.world_position.x), round(camera.world_position.z)) == (7, 10):
                                                            if self.door2.rotation_y <= -90:
                                                                self.door2.rotation_y += held_keys['e'] * time.dt * 50
                                                                self.open = True
                                                            elif self.door2.rotation_y >= 0:
                                                                self.door2.rotation_y -= held_keys['e'] * time.dt * 50
                                                                self.open = False
                                                            else:
                                                                if self.open == True:
                                                                    self.door2.rotation_y += held_keys['e'] * time.dt * 50
                                                                else:
                                                                    self.door2.rotation_y -= held_keys['e'] * time.dt * 50

        if self.is_enabled == True and self.player.position.y <= -30:
            self.player.position = (0, 5, 0)
            self.player.rotation = (0, 0, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        if self.is_enabled == True and held_keys["r"]:
            self.player.position = (0, 0, 0)
            self.player.rotation = (0, 0, 0)
            self.player.SPEED = normalSpeed
            self.player.jump_height = normalJump
            self.player.count = 0.0

        hit = raycast(self.player.position, self.player.down, distance = 2, ignore = [self.player, ])