import kivy
kivy.require('1.10.0')  # replace with your current kivy version !
from kivy.app import App
from kivy.config import Config
# Config.set('graphics', 'width', '200')
Config.set('graphics', 'height', '500')     # put your desired values instead of 200
class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()