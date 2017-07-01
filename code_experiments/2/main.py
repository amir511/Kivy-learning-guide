from __future__ import absolute_import, division, print_function
from builtins import *
import kivy
kivy.require('1.10.0')  # replace with your current kivy version !
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.adapters.listadapter import ListAdapter

# from kivy.config import Config
# # Config.set('graphics', 'width', '200')
# Config.set('graphics', 'height', '500')     # put your desired values instead of 200

class _InsideForm(BoxLayout):
    def __init__(self,**kwargs):
        super(_InsideForm,self).__init__(**kwargs)
        self.height = "100dp"
        self.size_hint_y = None
        self.add_widget(TextInput(text="Search"))
        btn = Button(text="Current Location")
        btn.size_hint_y = 1
        self.add_widget(btn)

class AddLocationForm(BoxLayout):
    def __init__(self,**kwargs):
        super(AddLocationForm,self).__init__(**kwargs)
        self.orientation = "vertical"
        # l = ListProperty(["Palo Alto, MX", "Palo Alto, US","Amir Anwar, Cairo", "Kivy kivy, Egypt"])
        # # adapter. = ListAdapter(data = ListProperty(["Palo Alto, MX", "Palo Alto, US","Amir Anwar, Cairo", "Kivy kivy, Egypt"]))

        # myListView = ListView().item_strings(l)
        self.add_widget(ListView(item_strings=["Palo Alto, MX", "Palo Alto, US","Amir Anwar, Cairo", "Kivy kivy, Egypt"]))
        self.add_widget(_InsideForm())

class MyApp(App):
    def build(self):
        return AddLocationForm()

if __name__ == '__main__':
    MyApp().run()