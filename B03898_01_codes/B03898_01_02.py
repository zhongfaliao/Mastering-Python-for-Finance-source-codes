""""
README
======
This file contains Python codes.
======
"""
from functools import partial
def greeting(my_greeting, name):
    print( "%s %s" % (my_greeting, name))

say_hello_to = partial(greeting, "Hello")
say_hello_to("World")
say_hello_to("Dog")
say_hello_to("Cat")
