from bearlibterminal import terminal
from clubsandwich.director import DirectorLoop, Scene

class BasicLoop2(DirectorLoop):
    def get_initial_scene(self):
        return MainMenuScene()

class MainMenuScene(Scene):
    def terminal_update(self, is_active=False):
        print(0, 0, "Press Enter to begin game, Esc to quit")

    def terminal_read(self, val):
        if val == terminal.TK_ENTER:
            self.director.push_scene(GameScene())
        elif val == terminal.TK_ESCAPE:
            self.director.pop_scene()

class GameScene(Scene):
    def terminal_update(self, is_active=False):
        print(0, 0, "You are playing the game, it is so fun! Press Esc to stop.")

    def terminal_read(self, val):
        if val == terminal.TK_ESCAPE:
            self.director.pop_scene()

if __name__ == '__main__':
    BasicLoop2().run()