import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder
from kivymd.app import MDApp
class MainApp(MDApp):
    def build(self):
        return MyGridLayout()
if __name__ == "__main__":
    MainApp().run()