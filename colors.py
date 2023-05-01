"""
File full of colors let's go
"""

from random import randint

class Colors:
    def __init__(self):
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)
        self.purple = (255, 0, 255)
        self.cyan = (0, 255, 255)
        self.orange = (255, 165, 0)
        self.pink = (255, 192, 203)
        self.brown = (165, 42, 42)
        self.grey = (128, 128, 128)
        self.dark_grey = (169, 169, 169)
        self.light_grey = (211, 211, 211)
        self.dark_red = (139, 0, 0)
        self.dark_green = (0, 100, 0)
        self.dark_blue = (0, 0, 139)
        self.dark_yellow = (184, 134, 11)
        self.dark_purple = (128, 0, 128)
        self.dark_cyan = (0, 139, 139)
        self.dark_orange = (255, 140, 0)
        self.dark_pink = (255, 20, 147)
        self.dark_brown = (139, 69, 19)

    def random(self):
        output = []
        for i in range(3):
            output.append(randint(0, 255))

        return tuple(output)