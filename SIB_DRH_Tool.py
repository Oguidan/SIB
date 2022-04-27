from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
from kivymd.app import MDApp
class GererLesListes(Screen):
    pass
class NewGameScreen(Screen):
    pass
# class LoadGameScreen(Screen):
    # pass
class ScreenManager(ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("SIB_DRH_Tool.kv")
MainApp().run()