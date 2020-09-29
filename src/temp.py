'''
Space for testing random stuff
'''

import sys
import os

print(
    os.path.realpath('.')
)

print(
    os.getcwd()
)

print(
    os.path.realpath(__file__)
)

print(
    __file__
)

print(
    os.path.realpath(os.path.dirname(__file__))
)
