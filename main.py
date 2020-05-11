from clubsandwich.blt.nice_terminal import terminal
from clubsandwich.director import DirectorLoop
from clubsandwich.geom import Size

from main_menu_scene import MainMenuScene

WINDOW_SIZE = Size(80, 46)

class GameLoop(DirectorLoop):
    def terminal_init(self):
        super().terminal_init()
        terminal.set("""
        window.resizeable=true;
        window.size={size.width}x{size.height}
        """.format(size=WINDOW_SIZE))

    def get_initial_scene(self):
        return MainMenuScene()    
   
if __name__ == '__main__':
 
  GameLoop().run()