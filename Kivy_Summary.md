# Kivy Summary and notes

## Important Packages Overview

**Core Package**

<!--TODO: add sample import usage-->
The code in the core package provides commonly used features, such as:
* Clock
You can use the clock to schedule timer events. Both one-shot timers and periodic
timers are supported
* Cache
If you need to cache something that you use often, you can use our class for that
instead of writing your own.
* Gesture Detection
We ship a simple gesture recognizer that you can use to detect various kinds of
strokes, such as circles or rectangles. You can train it to detect your own strokes.
* Kivy Language
The kivy language is used to easily and efficiently describe user interfaces.
* Properties
These are not the normal properties that you may know from python. They are
our own property classes that link your widget code with the user interface
description.

**UIX (Widgets & Layouts)**

The UIX module contains commonly used widgets and layouts that you can
reuse to quickly create a user interface.

* Widgets

Widgets are user interface elements that you add to your program to provide
some kind of functionality. They may or may not be visible. Examples
would be a file browser, buttons, sliders, lists and so on. Widgets receive
MotionEvents.

*Sample usage* 

`from kivy.uix.label import Label` or `from kivy.uix.button import Button`

* Layouts

You use layouts to arrange widgets. It is of course possible to calculate your
widgets’ positions yourself, but often it is more convenient to use one of our
ready made layouts. Examples would be Grid Layouts or Box Layouts. You
can also nest layouts.

*Sample usage* 

`from kivy.uix.gridlayout import Gridlayout` or `from kivy.uix import Button`


**Input Events ( Touches )**
<!--TODO: add sample import usage-->

Kivy abstracts different input types and sources such as touches, mice, TUIO or similar.
What all of these input types have in common is that you can associate a 2D onscreen-position
with any individual input event.
All of these input types are represented by instances of the Touch() class. A touch instance, or
object, can be in one of three states. When a touch enters one of these states, your program is
informed that the event occurred. The three states a touch can be in are:

* Down

A touch is down only once, at the very moment where it first appears.
* Move

A touch can be in this state for a potentially unlimited time. A touch does not have to be in this
state during its lifetime. A ‘Move’ happens whenever the 2D position of a touch changes.
* Up

A touch goes up at most once, or never. In practice you will almost always receive an up event
because nobody is going to hold a finger on the screen for all eternity, but it is not guaranteed.
If you know the input sources your users will be using, you will know whether or not you can
rely on this state being entered


**How a kivy Application works**

*imports*

```python
    import kivy
    kivy.require('1.10.0')  # replace with your current kivy version !
    from kivy.app import App
    from kivy.uix.label import Label
```
*Concept*
* Subclass the `App` class.
* Implement (override) its `build()` method.
* The `build()` method will return a `Widget` instance.
* This instance is the root of your **widget** tree.
* Then **instantiate** an object from this class.
* And finally call its `run()` method.
<span style=color:green>**That's it!** </span>

*Example Application*

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
*The Application life cycle*
Methods of the `App` class are fired in the following orders:
1. `run()`
2. `build()`
3. `on_start()`
4. Normal functioning of the application
5. Whenever something pauses the app the`on_stop()` and the `on_pause()` are fired, the `on_pause()` method either returns `True` or `False`
6. if `False` **Python** stops and application terminates
7. if `True`, the `on_resume()` is fired and app returns to step no. 4


*Notes*

* A kivy application must inheret from `App` class.
* The `uix` kivy module is the one that contains user interface elements, i.e. widgets and layouts.
* In the `build` function, we should return the ***Root widget***.
* you can add `self.title` in the `build` method to add a title to the application windows.

*Passing a prepared Widget to the `app` class*

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
```

## Controling the environment
```python
import os
os.environ["KIVY_NO_CONSOLELOG"]= "1"   #This will prevent printing logs to the console
import kivy     # the previous line should be before importing kivy
```
## Config file
Location:  `C:\Users\Home_Folder\.kivy\config.ini`


