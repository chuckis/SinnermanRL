from clubsandwich.ui import (
  LabelView,
  ButtonView,
  LayoutOptions,
  UIScene,
)

from game_scene import GameMainScene

TITLE = """

         oo                                                                  
                                                                             
.d8888b. dP 88d888b. 88d888b. .d8888b. 88d888b. 88d8b.d8b. .d8888b. 88d888b. 
Y8ooooo. 88 88'  `88 88'  `88 88ooood8 88'  `88 88'`88'`88 88'  `88 88'  `88 
      88 88 88    88 88    88 88.  ... 88       88  88  88 88.  .88 88    88 
`88888P' dP dP    dP dP    dP `88888P' dP       dP  dP  dP `88888P8 dP    dP 



"""


ABOUT = """
Use <tab> and <return> to navigate menus.
""".strip()


class MainMenuScene(UIScene):
  def __init__(self, *args, **kwargs):
    views = [
      LabelView(
        TITLE[1:].rstrip(),
        layout_options=LayoutOptions.row_top(0.5)),
      LabelView(
        ABOUT,
        color_fg='#ffcb00',
        layout_options=LayoutOptions.centered('intrinsic', 'intrinsic').with_updates(top=28)),
      ButtonView(
        text="Play", callback=self.play,
        layout_options=LayoutOptions.row_bottom(10).with_updates(
          left=0.2, width=0.2, right=None)),
      ButtonView(
        text="Quit", callback=lambda: self.director.pop_scene(),
        layout_options=LayoutOptions.row_bottom(10).with_updates(
          left=0.6, width=0.2, right=None)),
    ]
    super().__init__(views, *args, **kwargs)

  def play(self):
    self.director.push_scene(GameMainScene())
