#!/usr/bin/python3

import zielone_koktajle

import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.widget import Widget


class MainScreen(BoxLayout):

    def __init__(self, *args):
        super().__init__(*args)
        self.ingredients_sites = []
        self.count = 0

    def on_state(self, state, ingredient_name):
        if state:
            # dd sites to the list "ingredient_sites" by extracting value of the key from dictionary
            self.ingredients_sites.extend(zielone_koktajle.get_ing_from_csv().get(ingredient_name))
            self.count += 1

            #display in TextInput result from ingredient_sites
            self.display.text = str(zielone_koktajle.result(self.ingredients_sites, self.count))
        else:
            for i in (zielone_koktajle.get_ing_from_csv().get(ingredient_name)):
                if i in self.ingredients_sites:
                    self.ingredients_sites.remove(i)
            self.count -= 1
            self.display.text = str(zielone_koktajle.result(self.ingredients_sites, self.count))


class ZieloneKoktajleChApp(App):
     def build(self):
        self.title = "Zielone koktajle - index"
        return MainScreen()


if __name__ == "__main__":
    ZieloneKoktajleChApp().run()