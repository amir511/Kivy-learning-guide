# Kivy Summary and notes

<span style=color:blue> 

## ***How a kivy program works***
</span>

-------------

## imports

```python
    import kivy
    kivy.require('1.10.0')  # replace with your current kivy version !
    from kivy.app import App
    from kivy.uix.label import Label

```
## Concept
* Subclass the `App` class.
* Implement (override) its `build()` method.
* The `build()` method will return a `Widget` instance.
* This instance is the root of your **widget** tree.
* Then **instantiate** an object from this class.
* And finally call its `run()` method.
<span style=color:green>**That's it!** </span>

```python
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.label import Label

class Amir_App(App):
    def build(self):
        return Label(text='Hello World')
mero = Amir_App()
mero.run()
```

## Notes

* A kivy application must inheret from `App` class.
* The `uix` kivy module is the one that contains user interface elements, i.e. widgets and layouts.
* In the `build` function, we should return the ***Root widget***.
* you can add `self.title` in the `build` method to add a title to the application windows.

## Passing a prepared Widget to the `app` class:

```python
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout  # The Grid Layout will be the container of the prepared widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput    # This is a user input widget

class Login_screen(GridLayout):     # Now defining the prepared widget
    def __init__(self,**kwargs):
        super(Login_screen,self).__init__(**kwargs)     # this line is mandatory or the app won't work, this is related to the base class
        self.cols = 2   # this setups the GridLayout to have two have two columns, the other widgets will be inserted in those columns
        self.add_widget(Label(text = 'User Name'))      # This method inserts a Label widget in the first row of the first column
        self.username = TextInput(multiline=False)      # This will give our Login_screen class an attribute called username
        self.add_widget(self.username)  # with the previous line, this can e done in only one line: 
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
```

