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
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window



class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.size = (1400, 800)
        self.ingredients_sites = []
        self.count = 0

    def display_text(self, count):
        # displaying result in TextInput from ingredient_sites
        result = zielone_koktajle.result(self.ingredients_sites, count)
        if result:
            self.display.text = ", ".join(result)
        else:
            self.display.text = ""
            self.display.hint_text = "brak wspolnych stron.."


    def on_state(self, state, ingredient_name):
        if state == "down":
            # dd sites to the list "ingredient_sites" by extracting value of the key from dictionary
            self.ingredients_sites.extend(zielone_koktajle.get_ing_from_csv().get(ingredient_name))
            self.count += 1
            self.display_text(self.count)

        if state == "normal":
            for i in (zielone_koktajle.get_ing_from_csv().get(ingredient_name)):
                if i in self.ingredients_sites:
                    self.ingredients_sites.remove(i)
            self.count -= 1
            self.display_text(self.count)


class ZieloneKoktajleApp(App):
     def build(self):
        self.title = "Zielone koktajle - index"
        return MainScreen()


if __name__ == "__main__":
    myapp = ZieloneKoktajleApp()
    myapp.run()