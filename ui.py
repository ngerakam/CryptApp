from __future__ import print_function

__author__ = 'Dennis Kamau Ngera'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix import *
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class MainScreen(Screen):
    pass

class CipherScreen(Screen):
    pass

class ManagerScreen(ScreenManager):
    def __init__(self, **kwargs):
        super(ManagerScreen, self).__init__(**kwargs)
    pass

mixer = Builder.load_file('multiple.kv')

class Many(App):
    def build(self):
        return mixer

if __name__ == '__main__':
    joy = Many()
    joy.run()