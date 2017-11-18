from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar
from kivy.uix.gridlayout import GridLayout


class MyActionBar(ActionBar):
    def __init__(self, **kwargs):
        super(MyActionBar, self).__init__(**kwargs)

        self.pos_hint = {'top': 1}

class HouseShell(GridLayout):
    def __init__(self, **kwargs):
        super(HouseShell, self).__init__(**kwargs)
        self.rows = 1
        self.cols = 1
        self.size_hint = (1, .94)
        self.pos_hint = {'center_x': .5, 'center_y': .45}

class HouseLayout(GridLayout):
    house_list = ['one', 'two', 'three', 'four']
    def __init__(self, **kwargs):
        super(HouseLayout, self).__init__(**kwargs)
        self.rows = 12
        self.cols = 1
        self.size_hint_y = 1.5

class HouseButton(Button):
    def __init__(self, **kwargs):
        super(HouseButton, self).__init__(**kwargs)
        self.font_size = 30
        self.font_pos = 'left'
        self.background_color = [0, 0, 0, 0]




