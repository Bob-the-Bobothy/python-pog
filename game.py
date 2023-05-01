"""
Crappy pong clone made with pygame
"""

import pygame
from pygame.locals import *
from sys import exit
from colors import Colors

colors = Colors()

pygame.init()

class Screen:   
    def __init__(self):
        self.x = 640
        self.y = 480
        self.size = (self.x, self.y)

    def screen(self):
        return pygame.display.set_mode(self.size, 0, 32)
    
    def caption(self):
        return pygame.display.set_caption("pogger")
    
screen = Screen()
screen.screen()
screen.caption()

class Paddle1:
    def __init__(self):
        self.x = 20
        self.y = 200
        self.width = 10
        self.height = 60
        self.speed = 10
        self.score = 0
    
    def draw(self):
        return pygame.draw.rect(screen.screen(), (255, 255, 255), (self.x, self.y, self.width, self.height))
    
    def move(self):
        key = pygame.key.get_pressed()
        if key[K_w] and self.y > 0:
            self.y -= self.speed
        elif key[K_s] and self.y < (screen.y - self.height):
            self.y += self.speed

paddle1 = Paddle1()

class Paddle2:
    def __init__(self):
        self.width = 10
        self.height = 60
        self.speed = 10
        self.score = 0
        self.x = 620
        self.y = (screen.y / 2) + (self.height / 2)
    
    def draw(self):
        return pygame.draw.rect(screen.screen(), (255, 255, 255), (self.x, self.y, self.width, self.height))
    
    def move(self):
        key = pygame.key.get_pressed()
        if key[K_UP] and self.y > 0:
            self.y -= self.speed
        elif key[K_DOWN] and self.y < (screen.y - self.height):
            self.y += self.speed

paddle2 = Paddle2()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    screen.screen().fill(colors.light_grey)

    paddle1.draw()
    paddle1.move()
    paddle2.draw()
    paddle2.move()

    pygame.display.update()