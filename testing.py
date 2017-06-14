import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# Subclassing The layout super class
class MyScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MyScreen, self).__init__(**kwargs)
# Now programatically defining layout properties and adding widgets to it
# This should not be done if you have already defined the properties and added widgets in the .kv file
# It is easier of course to do it using the kv lang, but I am showing it here for reference.
    ''' 
        self.rows = 2   
        self.cols = 2
        self.padding = 10
        self.spacing = 10
        self.add_widget(Label(text='label widget')) # adding a widget on the fly
        #Adding widget on two steps
        self.text1 = TextInput(multiline=False)
        self.add_widget(self.label1)
    '''
# Finished the programmatical approach
# Instantiating the App class to make our application
class MyApp(App):   # this class name should always be like this: SomenameApp
    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyApp().run() #Instantiating the app on the fly and calling its run method