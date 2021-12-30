#!/usr/bin/python3

"""
Program is an addition for a book "Zielone koktajle - 365 przepisów".
Program helps to organize concluded recipes: reader can choose ingredients and application will show recipes's common pages with chosen ingredients. 
"""

import zielone_koktajle

import kivy
from kivy.config import Config
from kivy.metrics import dp, sp

kivy.require("1.9.0")
Config.set('graphics', 'window_state', 'maximized')
# Config.set('graphics', 'resizable', False) #window can't be maximized or minimized

# Config.set('graphics', 'position', 'custom')
# Config.set('graphics', 'top', '120')
# Config.set('graphics', 'left', '300')

# Config.set('graphics', 'width', '1400') #Window.size = (1400, 800) Window.size = dp(1400), dp(800)
# Config.set('graphics', 'height', '800')
# Config .set('graphics', 'minimum_width', '500')
# Config .set('graphics', 'minimum_hight', '500')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
# from kivy.uix.button import Button
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.label import Label
# from kivy.uix.textinput import TextInput
# from kivy.uix.widget import Widget
# from kivy.lang import Builder
# from kivy.properties import ObjectProperty, StringProperty

class MainScreen(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ingredients_sites = []
        self.tbn_press = 0

    def display_text(self, tbn_press):
        # displaying result in TextInput from ingredient_sites
        result = zielone_koktajle.result(self.ingredients_sites, tbn_press)
        if result:
            self.display.text = ",  ".join(result)
        else:
            self.display.text = ""
            if tbn_press == 0:
                self.display.hint_text = "wybierz składniki.."
            else:
                self.display.hint_text = "brak wspólnych stron.."


    def on_state(self, togglebutton):
        tb = togglebutton
        print(tb.size)
        if tb.state == "down":
            # dd sites to the list "ingredient_sites" by extracting value of the key from dictionary
            self.ingredients_sites.extend(zielone_koktajle.get_ing_from_csv().get(tb.text))
            self.tbn_press += 1
            self.display_text(self.tbn_press)

        if tb.state == "normal":
            for i in (zielone_koktajle.get_ing_from_csv().get(tb.text)):
                if i in self.ingredients_sites:
                    self.ingredients_sites.remove(i)
            self.tbn_press -= 1
            self.display_text(self.tbn_press)


class ToggleButtons(StackLayout):
    # adding togllebuttons with ingredients
    category_dict = {1: "owoce", 2: "warzywa", 3: "napoje", 4: "inne"}
    inst_count = 0

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        ToggleButtons.inst_count += 1
        for i in zielone_koktajle.prepare_csv():
            if i[0] == self.category_dict[self.inst_count]:
                tgbtn = ToggleButton(text = i[1])
                self.add_widget(tgbtn)


class ZieloneKoktajleApp(App):
     def build(self):
        self.title = "Zielone koktajle - index"
        return MainScreen()


if __name__ == "__main__":
    myapp = ZieloneKoktajleApp()
    myapp.run()