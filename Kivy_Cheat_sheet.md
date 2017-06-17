# Kivy Framework Cheat Sheet

In all applications the following imports should be done:

```python

import kivy
kivy.require('1.10.0')  # replace with your current kivy version !
from kivy.app import App

```

Then import the layout(s) that needs to be used:

*e.g.:*

```python

from kivy.uix.gridlayout import GridLayout

```

Then the import the widget(s) that will be used:

*e.g.:*

```python

from kivy.uix.textinput import TextInput

```

## Typical Python `main.py` file:

```python
import kivy
kivy.require('1.10.0')
from kivy.app import App
from kivy.uix.'''somelayout''' import '''SomeLayout'''

class TypicalScreen('''SomeLayout'''):
    def __init__(self,**kwargs):
        super(TypicalScreen, self).__init__(**kwargs)

class TypicalApp(App):
    def build(self):
        return MyScreen()

if __name__ == '__main__':
    MyApp().run()

```

## Typical Kivy `typical.kv` file:

```yaml

<TypicalScreen>:
    SomeLayout:
        someproperty:
        someproperty:
        someproperty:

        SomeWidget:
            someproperty:
            someproperty:
            someproperty:

        SomeAnotherWidget:
            someproperty:
            someproperty:
            someproperty:
            someproperty:
            someproperty:

```

## Available layouts

from kivy.uix.anchorlayout AnchorLayout

from kivy.uix.floatlayout import FloatLayout

GridLayout

from kivy.uix.pagelayout import PageLayout

from kivy.uix.relativelayout import RelativeLayout

from kivy.uix.scatterlayout import ScatterLayout

from kivy.uix.stacklayout import StackLayout

### GridLayout

* Python:

```python

from kivy.uix.gridlayout import GridLayout

```

* Kivy:

```yaml

GridLayout:
    spacing: 10     #Spacing between children i.e.: widgets, can be : x,y (horizontal spacing, vertical spacing), or can be one argument only, defaults to 0,0 if not added
    padding: 10     # Padding between the layout box and it's children, can be 4 arguments (left,top,right,bottom), or 2(horizontal,vertical), or one only, defaults to 0,0,0,0 if not added
    cols: 2     # Number of columns in the grid, defaults to 0
    rows: 2     # Number of rows in the grid, defaults to 0
    col_default_width: 0    # Default minimum size to use for a column, defaults to 0
    row_default_height: 0   # Default minimum size to use for row, defaults to 0
    col_force_default: False    # If True, ignore the width and size_hint_x of the child and use the default column width, default is False
    row_force_default: False    # If True, ignore the height and size_hint_y of the child and use the default row height, default is False

```

<!--TODO: list every layout-->

## Available Classical Widgets

kivy.uix.label

kivy.uix.button

kivy.uix.checkbox

kivy.uix.image

kivy.uix.slider

kivy.uix.progressbar

kivy.uix.textinput

kivy.uix.togglebutton

kivy.uix.switch

kivy.uix.video

<!--TODO:Add the description of every widget-->

## Available Complex Widgets

kivy.uix.bubble

kivy.uix.dropdown

kivy.uix.

kivy.uix.popup

kivy.uix.spinner

kivy.uix.listview

kivy.uix.tabbedpanel

kivy.uix.videoplayer

kivy.uix.vkeyboard

## Behaviours Widgets

api-kivy.uix.scatter

api-kivy.uix.stencilview

## Screen Manager

api-kivy.uix.screenmanager

