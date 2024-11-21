import random

class Level:
    def __init__(self):
        self.population = []
        for i in range(100):
            self.population.append(i + 1)