#!/usr/bin/kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class MenuScreen(Screen):
    pass

class NewGameScreen(Screen):
    pass

class LoadGameScreen(Screen):
    pass

class ScreenManager(ScreenManager):
    pass

buildKV = Builder.load_file("test0.kv")

class ASCIILifeApp(App):
    def build(self):
        return buildKV

if __name__ == "__main__":
    ASCIILifeApp().run()
