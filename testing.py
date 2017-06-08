import os
os.environ["KIVY_NO_CONSOLELOG"]= "1"
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout  # The Grid Layout will be the container of the prepared widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput    # This is a user input widget

class Login_screen(GridLayout):     # Now defining the prepared widget
    def __init__(self,**kwargs):
        super(Login_screen,self).__init__(**kwargs)     # this line is mandatory or the app won't work, this is related to the base class
        self.cols = 2   # this setups the GridLayout to have two columns, the other widgets will be inserted in those columns
        self.add_widget(Label(text = 'User Name'))      # This method inserts a Label widget in the first row of the first column
        self.username = TextInput(multiline=False)      # This will give our Login_screen class an attribute called username
        self.add_widget(self.username)  # with the previous line, this can be done in only one line: 
        # self.add_widget(TextInput(multiline=False))
        self.add_widget(Label(text='Password')) 
        self.password = TextInput(password=True,multiline=False)
        self.add_widget(self.password)  # inserting last widget in the second row in the second column

class Amir_App(App):
    def build(self):
        self.title = 'My First Kivy Application'    # adding a title to the window
        return Login_screen()   # returning a widget (our prepared Login_screen widget)

mero = Amir_App()
mero.run()  # Can be done like this: Amir_App().run(): instantiation on the fly and calling run method immediately
