from ursina import *
from player import Player
from block import *
from worlds.world1 import World1
from pause import PauseMenu

application.development_mode = True

app = Ursina(borderless = False)

window.title = "Game"
window.fps_counter.disable()

window.exit_button = False

normalSpeed = 2
boostSpeed  = 3

normalJump = 0.3

player = Player((0, 5, 0), 'cube', controls="wasd") 
player.SPEED = normalSpeed
player.jump_height = normalJump
player.position = (0, 5, 0)
player.rotation = (0, 0, 0)

player.enable()
mouse.locked = True

world1 = World1()
world1.player = player

sky = Sky(texture = "sky")

light = PointLight(position = (500, 500, 500), color = color.white)
AmbientLight(color = color.rgba(100, 100, 100, 10))

def reset_player():
    player.position = (0, 10, 0)
    player.SPEED = normalSpeed
    player.jump_height = normalJump
    camera.rotation_z = 0

def input(key):
    if key == "escape":
        mouse.locked = False
        player.disable()
        
        p = PauseMenu()
        p.player = player
        p.world1 = world1

def update():

    ray = raycast(player.position, player.down, distance = 3, ignore = [player, ])

app.run()