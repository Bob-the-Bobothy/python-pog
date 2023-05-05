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

    def random(self, min=0, max=255):
        output = []
        for i in range(3):
            output.append(randint(min, max))

        return tuple(output)
    
    def lighten(self, color, amount):
        output = []
        for i in range(3):
            output.append(color[i] + amount)
            if output[i] > 255:
                output[i] = 255

        return tuple(output)
    
    def darken(self, color: tuple, amount: int):
        output = []
        for i in range(3):
            output.append(color[i] - amount)
            if output[i] < 0:
                output[i] = 0

        return tuple(output)