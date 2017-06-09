from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

class Screen(GridLayout):
    def __init__(self,**kwargs):
        return super(Screen,self).__init__(**kwargs)
        output = StringProperty(Label)
        inputt = StringProperty(TextInput)
    # def get_text(self,text):
    #     output.text = inputt.text


class TestApp(App):
    def build(self):
        return Screen()

TestApp().run()