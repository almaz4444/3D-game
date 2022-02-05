from ursina import *

# Home
class Home(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (8, 8, 8)):
        super().__init__(
            model = "home",
            texture = "house",
            position = position,
            collider = 'mesh',
            rotation = rotation,
            scale = scale
        )

# Home Door
class Door(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (8, 8, 8)):
        super().__init__(
            model = "door",
            texture = "house",
            collider = 'mesh',
            rotation = rotation,
            position = position,
            scale = scale
        )

# Grass
class GrassBlock(Entity):
    def __init__(self, position = (0, 0, 0), rotation = (0, 0, 0), scale = (1, 1, 1)):
        super().__init__(
            model = "grass",
            texture = "grass",
            collider = 'mesh',
            position = position,
            rotation = rotation,
            scale = scale
        )

# Sun
class Sun(Entity):
    def __init__(self, position = (100, 100, 100), rotation = (0, 0, 0), scale = (100, 100, 100)):
        super().__init__(
            model = "sun",
            texture = "sun",
            collider = 'mesh',
            position = position,
            rotation = rotation,
            scale = scale
        )