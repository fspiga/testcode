'''Functions for compatibility with python <2.6.'''

# Import from the sets module if sets are not part of the language.
try:
    set(['abc'])
except NameError:
    from sets import Set as set

# Any and all don't exist in python <2.5. Define our own in pure python.
try:
    all([])
except NameError:
    def all(iterable):
        '''all(iterable) -> bool

Return True if bool(x) is True for all values x in the iterable.'''
        for val in iterable:
            if not val:
                return False
        return True
try:
    any([])
except NameError:
    def any(iterable):
        '''any(iterable) -> bool

Return True if bool(x) is True for any x in the iterable.'''
        for val in iterable:
            if val:
                return True

# math.isnan was introduced in python 2.6, so need a workaround for 2.4 and 2.5.
try:
    from math import isnan
except ImportError:
    def isnan(val):
        '''Return True if x is a NaN (not a number), and False otherwise.

Replacement for math.isnan for python <2.6.
This is not guaranteed to be portable, but does work under Linux.'''
        return type(val) is float and val != val
