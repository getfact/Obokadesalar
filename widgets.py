from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.actionbar import ActionBar
from kivy.uix.listview import ListView
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.clock import Clock

class TestListView(ListView):
    def __init__(self, **kwargs):
        super(TestListView, self).__init__(**kwargs)
        self.item_strings = ['nova', 'gayhuset']

class TestCarousel(Carousel):
    def __init__(self, **kwargs):
        super(TestCarousel, self).__init__(**kwargs)

        self.size_hint = (1, .1)
        self.pos_hint = {'center_x': .5, 'center_y': .8}

class TestLabel(Label):
    def __init__(self, **kwargs):
        super(TestLabel, self).__init__(**kwargs)

        self.size_hint = (1, .5)
        self.pos_hint = {'center_x': .5, 'center_y': .8}
        self.text = 'hehe'
        self.counter = 0
        Clock.schedule_interval(self.update, 1)

    def update(self, *args):
        self.counter += 1
        self.text = str(self.counter)


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



