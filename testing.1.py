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
from kivy.properties import StringProperty
from kivy.event import EventDispatcher
import time
Config.set('graphics','width',500)
Config.set('graphics','height',200)

class Timer(EventDispatcher):
    now = StringProperty('')
    def __init__(self,**kwargs):
        super(Timer, self).__init__(**kwargs)
        self.now = str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])

fgdfgdg
class MyScreen(GridLayout):
    timer = Timer()
    def __init__(self,**kwargs):
        super(MyScreen, self).__init__(**kwargs)
        self.ids.label.text = self.timer.now
        self.repeat_this(1)
                        
    def repeat_this(self,interval):
        Clock.schedule_interval(self.update_now,interval)

    def update_now(self,dt):   
        now = str(time.localtime()[3])+':'+str(time.localtime()[4])+':'+str(time.localtime()[5])
        self.timer.now = now
        
    

class MyApp(App):   # this class name should always be like this: SomenameApp
    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyApp().run() #Instantiating the app on the fly and calling its run method
