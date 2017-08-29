#!/usr/bin/python3
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.config import Config
from kivy.clock import Clock
import time
Config.set('graphics','width',500)
Config.set('graphics','height',200)

class MyScreen(GridLayout):
    now = str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])
    trigger = None
    def __init__(self,**kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.repeat_this(1)
        self.create_trigger()
        self.trigger()
        Clock.schedule_once(self.fill_label,12)
        Clock.schedule_once(self.clear_label,14)

    def repeat_this(self,interval):
        Clock.schedule_interval(self.print_now,interval)
    
    def print_now(self,dt):
        self.update_now()
        self.ids.interval.text = self.now

    def update_now(self):   
        now = str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])
        self.now = now
    
    
    def create_trigger(self):
        global trigger
        trigger = Clock.create_trigger(self.clear_label, 10)
    
    
    def clear_label(self,dt):
        self.ids.label.text = ""
    
    def trigger(self):
        global trigger
        trigger()
    
    def fill_label(self,dt):
        self.ids.label.text = "New text added"

class MyApp(App):   # this class name should always be like this: SomenameApp
    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyApp().run() #Instantiating the app on the fly and calling its run method
