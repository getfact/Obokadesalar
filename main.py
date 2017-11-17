from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from widgets import TestCarousel, TestListView, HouseShell, HouseLayout, MyActionBar

Builder.load_file('layout.kv')

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)


class Search(Screen):
    pass

class About(Screen):
    pass

class Controller(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Home(name='home'))
        sm.add_widget(Search(name='search'))
        sm.add_widget(About(name='about'))
        return sm

c = Controller()
c.run()
