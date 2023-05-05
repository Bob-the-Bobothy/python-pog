"""
Crappy pong clone made with pygame
"""

import pygame
from pygame.locals import *
from sys import exit
from colors import Colors
import random

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
display = screen.screen()
screen.screen()
screen.caption()

class Paddles:
    def __init__(self):
        self.width = 10
        self.height = 70
        self.speed = 7.5
        self.score = 0
        self.spacing = 40
        self.center = (screen.y / 2) - (self.height / 2)
        self.color = colors.white
    
    def rect(self, x, y):
        return pygame.Rect(x, y, self.width, self.height)
        
paddles = Paddles()

class Paddle1(Paddles):
    def __init__(self):
        self.x = paddles.spacing
        self.y = paddles.center
        self.rect = paddles.rect(self.x, self.y)
    
    def draw(self):
        self.rect = paddles.rect(self.x, self.y)
        return pygame.draw.rect(display, paddles.color, self.rect)
    
    def move(self):
        self.rect = paddles.rect(self.x, self.y)
        key = pygame.key.get_pressed()
        if key[K_w] and self.y > 0:
            self.y -= paddles.speed
        elif key[K_s] and self.y < (screen.y - paddles.height):
            self.y += paddles.speed

paddle1 = Paddle1()

class Paddle2(Paddles):
    def __init__(self):
        self.x = screen.x - (paddles.spacing + paddles.width)
        self.y = paddles.center
        self.rect = paddles.rect(self.x, self.y)
    
    def draw(self):
        self.rect = paddles.rect(self.x, self.y)
        return pygame.draw.rect(display, paddles.color, self.rect)
    
    def move(self):
        self.rect = paddles.rect(self.x, self.y)
        key = pygame.key.get_pressed()
        if key[K_UP] and self.y > 0:
            self.y -= paddles.speed
        elif key[K_DOWN] and self.y < (screen.y - paddles.height):
            self.y += paddles.speed

paddle2 = Paddle2()

class Ball:
    def __init__(self):
        self.x = screen.x / 2
        self.y = screen.y / 2
        self.radius = 10
        self.speed = {
            "x": random.choice([-5, 5]),
            "y": 0,
        }
        
    def draw(self):
        return pygame.draw.circle(display, colors.darken(colors.green, 50), (self.x, self.y), self.radius)
    
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
            
    def move(self):
        if pygame.Rect.colliderect(self.rect(), paddle1.rect) or pygame.Rect.colliderect(self.rect(), paddle2.rect):
           self.speed["x"] =- self.speed["x"]
           self.speed["y"] =- self.speed["y"]
           
        self.x += self.speed["x"]
        self.y += self.speed["y"]
        
    def death(self):
        if self.x < 0 or self.x > screen.x:
            return False
        else:
            return True

ball = Ball()        

clock = pygame.time.Clock()

running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    display.fill(colors.lighten(colors.cyan, 75))

    paddle1.draw()
    paddle1.move()
    paddle2.draw()
    paddle2.move()
    
    ball.draw()
    ball.move()

    pygame.display.update()
    
    running = ball.death()
