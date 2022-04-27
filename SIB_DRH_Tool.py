from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty
class GererLesListes(Screen):
    pass
class ImprimerDesFiches(Screen):
    pass
# class LoadGameScreen(Screen):
    # pass
class ScreenManager(ScreenManager):
    pass
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file("SIB_DRH_Tool.kv")
MainApp().run()