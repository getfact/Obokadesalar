from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty

from widgets import HouseShell, HouseLayout, MyActionBar
import datafetcher
from SearchData import *

Builder.load_file('layout.kv')

class Home(Screen):

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)
        
    def set_text(self, location):
        
        results = ""
        
        if location == "Novahuset":
            df_nova = datafetcher.DataFetcher(novahuset_rooms_url, novahuset_rooms)
            results = df_nova.build_output()
        
        else:
            results = "Switch error."
        self.manager.get_screen('search').labelText = results

class Search(Screen):
    labelText = StringProperty('My label')
    
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
