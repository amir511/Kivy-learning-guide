# Kivy Summary and notes

<small style=color:grey> *Sources used:*</small>

<small style=color:grey> 

- "KIVY - A Framework for Natural User Interfaces
    
    Nik Klever,
    Faculty of Computer Sciences,
    University of Applied Sciences Augsburg"

- Kivy Official Documentation

- Creating Apps in Kivy, Dusty Phillips

</small>


## Important Packages Overview

**Core Package**

<!--TODO: add sample import usage-->
The code in the core package provides commonly used features, such as:
* Clock

    You can use the clock to schedule timer events. Both one-shot timers and periodic timers are supported
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

*Concept*
* Import the required kivy modules in the python file
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
* All user interface elements are called widgets, i.e. **Layouts are a form of widgets**
* In the `build` function, we should return the ***Root widget***.
* you can add `self.title` in the `build` method to add a title to the application windows.

*Let's now look at another application that will prepare a widget first then pass it to `app` class*

>Tip: Read carefully the comments in the code to understand the function of every line

```python
import kivy
kivy.require('1.10.0')  # Replace with your kivy version if needed
from kivy.app import App    #This is always required, your app will have to be a subclass of the App class
from kivy.uix.gridlayout import GridLayout  # The Grid Layout will be the container of the prepared widget
from kivy.uix.label import Label    # The Label widget is a widget that displays text
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

Up till now, we have been using the kivy framework from inside python, which can be sufficient and does the required job

But kivy has an interesting way to do it in a simpler way, using a markup language called `kivy language` or `kvlang`

*Now lets look at an example which utilizes the ***Kivy*** language*

***Python Code***

*usually the python file is named `main.py` this is not mandatory but in case of packaging your application for other platforms this is crucial*
```python
# Imports
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# Subclassing The layout super class
class MyScreen(GridLayout):
    def __init__(self,**kwargs):v
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
        return MyScreen()   #instantiating MyScreen and calling its constructor (__init__) method

if __name__ == '__main__':
    MyApp().run() #Instantiating the app on the fly and calling its run method
```
***Kv lang***

>*File name should be: `my.kv` ; i.e. whatever you call your App class, you will strip the `App` word from it and name your kivy file with the first word in lowercase letters, In that way, kivy will be able to connect the kivy file with the appropriate class in python, also make sure that it will be in the same directory with the `main.py`*

```yaml
<MyScreen>:  # Every custom class should be represented between tow angular `<>` brackets
# Here MyScreen is a custom class and the root widget in the kivy file at the same time
    rows: 2
    cols: 2
    spacing: 10
    TextInput:  #  This is another widget that is a child of the root widget MyScreen
        id: text1
        multiline: False
    Label:  #  This is another widget that is a child of the root widget MyScreen
        text: 'label widget'
```
***Important Keywords***

There are three important keywords specific to Kv language:

* `app`: always refers to the instance of your application.
* `root`: refers to the base widget/template in the current rule
* `self` : always refer to the current widget

***Triggering events in the Kv lang (Event dispatching)***

Every class (either a widget or layout) has its own methods that can be overidden to trigger actions (other methods) that will do the desired behaviour of the app.

**for example:**

```yaml
<MyScreen>:
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

## Simplifying things up by using the power of kv lang

It is important to learn first the difficult way, and move then to the easy way.
So now that we have understood the internals of how a kivy program works, we can safely start using a more simple form that will do the same functionality with less complex code.

Preparing a custom widget and passing it to the subclass of `App` can be done on the fly in the kv lang as follows:

```yaml
MyScreen: #calling the root widget (preparing it later down here), this replaces the "return MyScreen()" line inside the "build" method of the "MyApp" class
<MyScreen@GridLayout>:  #this is equivalent to "class MyScreen(GridLayout)" in python
    rows: 2
    cols: 2
    spacing: 10
    TextInput:
        id: text1
        multiline: False
    Label:
        text: 'label widget'
```
So Since the kivy file have declared almost everything for us, the python code will only look like this:

```python
import kivy
kivy.require('1.10.0')
from kivy.app import App
# No need to import GridLayout as we did before, the kivy code already took care of that before!
class MyApp(App):
    pass

if __name__ == '__main__':
    MyApp().run()

```
As you have noticed, This python code is generic, and many changes can be done in the application through changing the kivy code only
offcourse, in more complex cases, you will need to add more code to the python file.
Go ahead and try it with many kivy files, just make sure that the kivy file will have the name `my.kv` as long as the `App` subclass has the name of `MyApp` as explained before.

## Scheduling

**What is Scheduling?**

If you have experience in Android development using Java, you already know that the UI is being executed in a memory thread calld the *Main Thread*, while other actions that are triggered in the background (e.g. Networking) are executed in another thread(s) called the *Worker Thread(s)*

Similarly, *Kivy* has a *Main loop* which resembles the Main Thread in Java, while other background jobs should be *Scheduled* to be triggered independently from the Main Loop

**Why Scheduling?**

If you request a web page to be loaded or downloaded while you are in the *Main Loop* (or in the *Main Thread*), The UI will hang or stutter or at least wait until the requested page be loaded then continue to function.

Scheduling is crucial to avoid UI hanging or bad user experience

**How Scheduling works?**

There are many ways to implement scheduling in kivy, but the common ways are:

```python
#....
from kivy.clock import Clock
# Method 1:
event = Clock.schedule_interval(function, interval)   # This method will trigger the function every some interval (seconds)

# But the function passed here must have a patameter of delta time as an argument in its signature

def function(dt):
    # some code
# the dt parameter is not needed to be used in the function

# Method 2:
event = Clock.schedule_once(function, delay)    # This will trigger function once only after some delay in seconds

# Again this function should have 'dt' as an argument
# Off course if this function is part of a class, it should look like this:

def function(self,dt):
    # some code

# If at some condition or at some point in your code, you need to disable the scheduled event, i.e. unschedule it, use:
event.cancel()

# Or:
Clock.unschedule(event)

# Or in the signature of the function itself, return False at the desired cancelation condition

```