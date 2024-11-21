"""
Goofy pong clone made with pygame
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
        self.speed = 6
        self.score = 0
        self.spacing = 40
        self.center = (screen.y / 2) - (self.height / 2)
        self.color = colors.white
    
    def rect(self, x, y):
        return pygame.Rect(x, y, self.width, self.height)
        
paddles = Paddles()

class PaddleL(Paddles):
    def __init__(self):
        self.x = paddles.spacing
        self.y = paddles.center
        self.rect = paddles.rect(self.x, self.y)
        self.speed = 0
    
    def draw(self):
        self.rect = paddles.rect(self.x, self.y)
        return pygame.draw.rect(display, paddles.color, self.rect)
    
    def move(self):
        self.rect = paddles.rect(self.x, self.y)
        key = pygame.key.get_pressed()
        if key[K_w] and self.y > 0:
            self.y -= paddles.speed
            self.speed =- paddles.speed
            
        elif key[K_s] and self.y < (screen.y - paddles.height):
            self.y += paddles.speed
            self.speed = paddles.speed

paddleL = PaddleL()

class PaddleR(Paddles):
    def __init__(self):
        self.x = screen.x - (paddles.spacing + paddles.width)
        self.y = paddles.center
        self.rect = paddles.rect(self.x, self.y)
        self.speed = 0
    
    def draw(self):
        self.rect = paddles.rect(self.x, self.y)
        return pygame.draw.rect(display, paddles.color, self.rect)
    
    def move(self):
        self.rect = paddles.rect(self.x, self.y)
        if ball.y < self.y + (paddles.height / 2) and self.y > 0:
            self.y -= paddles.speed
            self.speed =- paddles.speed
        
        if ball.y > self.y + (paddles.height / 2) and self.y < (screen.y - paddles.height):
            self.y += paddles.speed
            self.speed = paddles.speed

paddleR = PaddleR()

class Ball:
    def __init__(self):
        self.x = screen.x / 2
        self.y = screen.y / 2
        self.radius = 10
        self.speed = {
            "x": random.choice([-5, 5]),
            "y": random.randint(-1, 1),
        }
        self.speed_increase = .25
        
    def draw(self):
        return pygame.draw.circle(display, colors.darken(colors.green, 50), (self.x, self.y), self.radius)
    
    def rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius * 2, self.radius * 2)
            
    def move(self):
        if pygame.Rect.colliderect(self.rect(), paddleL.rect) or pygame.Rect.colliderect(self.rect(), paddleR.rect):
            self.speed["x"] =- self.speed["x"]
            if self.speed["x"] > 0:
                self.speed["x"] += self.speed_increase
                
            else:
                self.speed["x"] -= self.speed_increase
            
        if pygame.Rect.colliderect(self.rect(), paddleL.rect):
            self.speed["y"] = paddleL.speed / 3 + random.randint(-1, 1)
            
        if pygame.Rect.colliderect(self.rect(), paddleR.rect):
            self.speed["y"] = paddleR.speed / 3 + random.randint(-1, 1)
           
        if self.y - self.radius < 0 or self.y + self.radius > screen.y:
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

    paddleL.draw()
    paddleL.move()
    paddleR.draw()
    paddleR.move()
    
    ball.move()
    ball.draw()

    pygame.display.update()
    
    running = ball.death()
