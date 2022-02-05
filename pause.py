from ursina import *

class PauseMenu(Entity):
    def __init__(self):
        super().__init__(parent = camera.ui, ignore_paused = True)

        self.pause_menu = Entity(parent = self, enabled = True)
        self.player = None
        self.main_menu = None

        self.world1 = None

        def reset():
            self.pause_menu.disable()
            self.player.enable()
            mouse.locked = True

            if self.world1.is_enabled == True:
                self.player.position = (888, 12, 18)
                self.player.rotation = (0, -142, 0)

        def resume():
            self.player.enable()
            mouse.locked = True
            self.pause_menu.disable()

        resume_button = Button(text = "П р о д о л ж и т ь", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0.12, parent = self.pause_menu)
        reset_button = Button(text = "З а н о в о", color = color.black, scale_y = 0.1, scale_x = 0.3, y = 0, parent = self.pause_menu)
        quit_button = Button(text = "В ы х о д", color = color.black, scale_y = 0.1, scale_x = 0.3, y = -0.12, parent = self.pause_menu)
        quit_button.on_click = application.quit
        reset_button.on_click = Func(reset)
        resume_button.on_click = Func(resume)
