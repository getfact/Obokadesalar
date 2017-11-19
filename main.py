from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty

from widgets import HouseShell, HouseLayout, MyActionBar
from searchdata import *
import datafetcher

Builder.load_file('layout.kv')

class Home(Screen):

    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

    #Object creator.
    def __create_result(self, rooms_url, rooms):
        df = datafetcher.DataFetcher(rooms_url, rooms)
        output = df.build_output()
        return output
    
    #Gathering results to label.
    def set_result(self, location):
        
        results = ""
        #Location switch.
        if location == "Novahuset":
            results = self.__create_result(novahuset_rooms_url, novahuset_rooms)
        elif location == "Långhuset":
            results = self.__create_result(langhuset_rooms_url, langhuset_rooms)
        elif location == "Teknikhuset":
            results = self.__create_result(teknikhuset_rooms_url, teknikhuset_rooms)
        elif location == "Forumhuset":
            results = self.__create_result(forumhuset_rooms_url, forumhuset_rooms)
        elif location == "Prismahuset":
            results = self.__create_result(prismahuset_rooms_url, prismahuset_rooms)
        elif location == "Prismahuset2":
            results = self.__create_result(prismahuset_2_rooms_url, prismhuset_2_rooms)
        elif location == "PrismahusetG":
            results = self.__create_result(prismahuset_g_rooms_url, prismahuset_g_rooms)
        elif location == "Gymnastikhuset":
            results = self.__create_result(gymnastikhuset_rooms_url, gymnastikhuset_rooms)
        elif location == "Bilbergskahuset":
            results = self.__create_result(bilbergskahuset_rooms_url, Bilbergskahuset_rooms)
        elif location == "CampusUSO":
            results = self.__create_result(campus_uso_rooms_url, campus_uso_rooms)
        elif location == "Musikskolan":
            results = self.__create_result(musikskolan_rooms_url, musikskolan_rooms)
        elif location == "Biblioteket":
            results = self.__create_result(Biblioteket_g_rooms_url, Biblioteket_g_rooms)

        else:
            results = "Error: Switch default."

        self.manager.get_screen('search').result_text = results        

class Search(Screen):
    result_text = StringProperty('Error: Empty results.')
    
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
