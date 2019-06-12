#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import pygame #conda install -c cogsic pygame + install pygame with sudo apt-get install python-pygame
from  pygame.locals import *

pygame.init()

if not pygame.font:
    print("No fonts!")


# In[ ]:


screen_width = 500
screen_height = 500

def Screen(screen_width, screen_height, caption = "My PyGame"):
    win = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption(caption)
    return win

win = Screen(screen_width, screen_height)


# In[ ]:


class Elipse:
    def __init__(self, fminx, fmaxx, fminy, fmaxy, width, height, velocity=-1, color=(255,0,0), x = 0, y = 0):
        self.minx = fminx
        self.maxx = fmaxx
        self.miny = fminy
        self.maxy = fmaxy-10
        self.w = width
        self.h = height
        
        if self.w < self.h:
            self.w_save = self.w
            self.h_save = self.h
        else:
            self.w_save = self.h
            self.h_save = self.w
        
        if velocity < 0:
            self.v = max(self.w, self.h)
        else:
            self.v = velocity
            
        self.color = color
        
        self.x = x
        self.y = y
        self.d = 1
        
    def getColor(self):
        return self.color
    
    def getCoords(self):
        return (self.x, self.y, self.w, self.h)
    
    def getCenter(self):
        return (self.x + (self.w / 2), self.y + (self.h / 2))
    
    def getHead(self):
        if self.d == 1:
            return (self.x + (self.w / 2), self.y)
        if self.d == 2:
            return (self.x + (self.w / 2), self.y + self.h)
        if self.d == 3:
            return (self.x, self.y + (self.h / 2))
        if self.d == 4:
            return (self.x + self.w, self.y + (self.h / 2))
    
    def randomMove(self):
        self.d = random.randint(1,4)
        self.forward()
            
    def up(self):
        if self.y > self.miny + self.h:
            self.y -= self.v
            if self.w != self.w_save:
                self.w = self.w_save
            if self.h != self.h_save:
                self.h = self.h_save
        self.d = 1
        
    def right(self):
        if self.x < self.maxx - self.w:
            self.x += self.v
            if self.w != self.h_save:
                self.w = self.h_save
            if self.h != self.w_save:
                self.h = self.w_save
        self.d = 2
                
    def down(self):
        if self.y < self.maxy - self.h:
            self.y += self.v
            if self.w != self.w_save:
                self.w = self.w_save
            if self.h != self.h_save:
                self.h = self.h_save
        self.d = 3
                
    def left(self):
        if self.x > self.minx + self.w:
            self.x -= self.v
            if self.w != self.h_save:
                self.w = self.h_save
            if self.h != self.w_save:
                self.h = self.w_save
        self.d = 4
        
    def forward(self):
        if self.d == 1:
            self.up()
        if self.d == 2:
            self.right()
        if self.d == 3:
            self.down()
        if self.d == 4:
            self.left()
            
    def rightTurn(self): #90°
        self.d = self + 1 if self.d != 4 else 1
        
    def leftTurn(self): #90°
        self.d = self - 1 if self.d != 1 else 4
        
    def undraw(self, win):
        pygame.draw.ellipse(win, (0, 0, 0), self.getCoords())
        pygame.draw.line(win, (0, 0, 0), self.getCenter(), self.getHead())
        
    def draw(self, win):
        pygame.draw.ellipse(win, self.getColor(), self.getCoords())
        pygame.draw.line(win, (255,255,255), self.getCenter(), self.getHead())
        
class Tick:
    def __init__(self, win):
        self.t = 0
        self.win = win
        self.myfont = pygame.font.SysFont("Arial", 16)
        
    def tick(self):
        s = "Tick :"+str(self.t)
        label = self.myfont.render(s, 1, (0,0,0))
        self.win.blit(label, (0, 0))
        
        self.t += 1
        s = "Tick :"+str(self.t)
        
        label = self.myfont.render(s, 1, (0,255,0))
        self.win.blit(label, (0, 0))

# In[ ]:


run = True
ellipses = [Elipse(0, screen_width, 0, screen_height, 10, 15), 
            Elipse(0, screen_width, 0, screen_height, 10, 15, color=(255,0,255)), 
            Elipse(0, screen_width, 0, screen_height, 10, 15, color=(0,255,0))]

t = Tick(win)
while run:
    pygame.time.delay(500)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed() #https://www.pygame.org/docs/ref/key.html
    if keys[pygame.K_q]:
        run = False
        
    for e in ellipses:
        e.undraw(win)
        e.randomMove()
        e.draw(win)
    
    t.tick()
    
    pygame.display.update()
pygame.quit()

