# Kivy Summary and notes

<small style=color:grey> *Sources used:*</small>

<small style=color:grey> 

- "KIVY - A Framework for Natural User Interfaces
    
    Nik Klever,
    Faculty of Computer Sciences,
    University of Applied Sciences Augsburg"

- Kivy Official Documentation

</small>


## Important Packages Overview

**Core Package**

<!--TODO: add sample import usage-->
The code in the core package provides commonly used features, such as:
* Clock

    You can use the clock to schedule timer events. Both one-shot timers and periodic
timers are supported
* Cache

    If you need to cache something that you use often, you can use our class for that instead of writing your own.
* Gesture Detection

    Kivy ships a simple gesture recognizer that you can use to detect various kinds of strokes, such as circles or rectangles. You can train it to detect your own strokes.
* Kivy Language

    The kivy language is used to easily and efficiently describe user interfaces.
* Properties

    These are not the normal properties that you may know from python. They are our own property classes that link your widget code with the user interface description.

**UIX (Widgets & Layouts)**

The UIX module contains commonly used widgets and layouts that you can reuse to quickly create a user interface.

* Widgets

    Widgets are user interface elements that you add to your program to provide some kind of functionality. They may or may not be visible. Examples would be a file browser, buttons, sliders, lists and so on. Widgets receive MotionEvents.

*Sample Import usage* 

`from kivy.uix.label import Label` or `from kivy.uix.button import Button`

* Layouts

    You use layouts to arrange widgets. It is of course possible to calculate your
    widgets’ positions yourself, but often it is more convenient to use one of our
    ready made layouts. Examples would be Grid Layouts or Box Layouts. You
    can also nest layouts.

*Sample Import usage* 

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

class MyApp(App):
    def build(self):
        return Label(text='Hello World')
myKivy = MyApp()
myKivy.run()
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

*Let's look at another application that will prepare a widget first then pass it to `app` class*

Read carefully the comments in the code to understand the function of every line
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

class MyApp(App):
    def build(self):
        self.title = 'My First Kivy Application'    # adding a title to the window
        return Login_screen()   # returning a widget (our prepared Login_screen widget)

mykivy = MyApp()
mykivy.run()  # Can be done like this: MyApp().run(): instantiation on the fly and calling run method immediately
```
## Kivy Language
*Now lets look at an example which utilizes the ***Kivy*** language*

***Python Code***

*usually the python file is named `main.py` but this is just a convention and you can use any other name*
```python
# Imports
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
```
***Kv lang***
*file name should be: `my.kv`; i.e. whatever you call your App class, you will strip the `App` word from it and name your kivy file with the first word in lowercase letters*
```yaml
<MyScreen>:  # Every class name can be represented like this
    GridLayout:
        rows: 2
        cols: 2
        spacing: 10
        TextInput:
            id: text1
            multiline: False
        Label:
            text: 'label widget'
```
***Important Keywords***

There are three keywords specific to Kv language:

* `app`: always refers to the instance of your application.
* `root`: refers to the base widget/template in the current rule
* `self` : always refer to the current widget

***Triggering events in the Kv lang (Event dispatching)***

Every class (either a widget or layout) has its own methods that can be overidden to trigger actions (other methods) that will do the desired behaviour of the app.

**for example:**

```yaml
<MyScreen>:
    GridLayout:
        TextInput:
                id: text1
                multiline: False
                on_text_validate: root.do_come_action()
```
The `on_text_validate()` validate method is already defined in the `TextInput` class and no need to define it, it is only called from the kivy file

The `root` keyword, refers to the `MyScreen` class because it the parent layout that contains the `TextInput` widget, so the `do_some_action()` method should be defined in the `MyScreen` class

```python
class MyScreen(GridLayout):
    def __init__(self,**kwargs):
        super(MyScreen, self).__init__(**kwargs)
    
    def do_some_action(self,argument):
        pass #add the desired action here
```
If you want the widget itself to trigger the action, use: `self.do_some_action` in kivy, and define the method in a subclass of `TextInput`

And if you want the app itself to trigger the action, use: `app.do_some_action`, and define the method in the `App` subclass.



## Controling the environment
```python
import os
os.environ["KIVY_NO_CONSOLELOG"]= "1"   #This will prevent printing logs to the console
import kivy     # the previous line should be before importing kivy
```
## Config file
Location:  `C:\Users\Home_Folder\.kivy\config.ini`


