from ursina import *
import sys
from block import *
sys.path.append('../Parkour/')

normalSpeed = 1.5
normalJump = 0.2

class World1(Entity):
    def __init__(self):
        super().__init__()

        self.menu = Entity(parent = self, enabled = True)
        self.is_enabled = True
        self.player = None

        self.grass1 = GrassBlock((-6, -17, 3))

        self.door1 = Door((10.7, -9.4, -6.2))
        self.door2 = Door((10.4, -9.9, 6.8), scale=(5.9, 5.6, 5))
        self.home = Home((10, -10, 0))
        self.sun = Sun((500, 500, 500))
        self.table = Table((13.5, -10, 0))
        self.chair = Chair((13.5, -10, -1))

        self.is_sit = False
        self.sit = False
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

    def input(self, key):
        if key == 'e':
            if self.sit == True:
                self.player.position = (13.5, -9.3, -1.1)
                self.is_sit = True
        if key == 'q':
            if self.is_sit == True:
                self.player.position = (13.5, -9.3, -2)
                self.sit = False
                self.is_sit = False

    def update(self):
        print((round(camera.world_position.x), round(camera.world_position.z)))

        if (round(camera.world_position.x), round(camera.world_position.z)) == (10, -7) or \
            (round(camera.world_position.x), round(camera.world_position.z)) == (9, -7) or \
                (round(camera.world_position.x), round(camera.world_position.z)) == (10, -8) or \
                    (round(camera.world_position.x), round(camera.world_position.z)) == (11, -7) or \
                        (round(camera.world_position.x), round(camera.world_position.z)) == (10, -6) or \
                            (round(camera.world_position.x), round(camera.world_position.z)) == (9, -6) or \
                                (round(camera.world_position.x), round(camera.world_position.z)) == (11, -6) or \
                                    (round(camera.world_position.x), round(camera.world_position.z)) == (10, -5):
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

        if (round(camera.world_position.x), round(camera.world_position.z)) == (9, 7) or\
            (round(camera.world_position.x), round(camera.world_position.z)) == (10, 7) or\
                (round(camera.world_position.x), round(camera.world_position.z)) == (8, 7) or\
                    (round(camera.world_position.x), round(camera.world_position.z)) == (10, 6) or\
                        (round(camera.world_position.x), round(camera.world_position.z)) == (9, 6) or\
                            (round(camera.world_position.x), round(camera.world_position.z)) == (10, 5) or\
                                (round(camera.world_position.x), round(camera.world_position.z)) == (11, 6) or\
                                    (round(camera.world_position.x), round(camera.world_position.z)) == (11, 5) or\
                                        (round(camera.world_position.x), round(camera.world_position.z)) == (9, 5) or\
                                            (round(camera.world_position.x), round(camera.world_position.z)) == (10, 8):
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

        if (round(camera.world_position.x), round(camera.world_position.z)) == (13, -1) or\
            (round(camera.world_position.x), round(camera.world_position.z)) == (12, -1) or\
                (round(camera.world_position.x), round(camera.world_position.z)) == (12, -2) or\
                    (round(camera.world_position.x), round(camera.world_position.z)) == (14, -2) or\
                        (round(camera.world_position.x), round(camera.world_position.z)) == (13, -2):
                            self.sit = True                            
        else:
            self.sit = False

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

        hit = raycast(self.player.position, self.player.down, distance = 3, ignore = [self.player, self.home, self.grass1, ])