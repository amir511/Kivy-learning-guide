#!python
# Credit goes to the author of the snippet, Mathieu Virbel
# Source : https://github.com/kivy/kivy/wiki/Delayed-Work-using-Clock
from kivy.clock import Clock

def delayed_work(func, items, delay=0):
    '''Apply the func() on each item contained in items
    '''
    if not items:
        return
    def _delayed_work(*l):
        item = items.pop()
        if func(item) is False or not len(items):
            return False
        Clock.schedule_once(_delayed_work, delay)
    Clock.schedule_once(_delayed_work, delay)

#
# Usage example
#
def create_image(filename):
  image = Image(source=filename)
  my_container.add_widget(image)

items = ['img1.png', 'img2.png', 'toto.png', 'azdmlk.png']
delayed_work(create_image, items)