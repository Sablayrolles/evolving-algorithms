#!/usr/bin/env python
# coding: utf-8

import random
import pygame #conda install -c cogsic pygame ou pip install pygame + install pygame with sudo apt-get install python-pygame
from  pygame.locals import *
import pprint

pygame.init()

if not pygame.font:
    print("No fonts!")

#Coordonées : 0;0 coin haut
# up vers le haut et droite vers la droite dans une fenetre

class Elipse:
    def __init__(self, fminx, fmaxx, fminy, fmaxy, width, height, env, velocity=-1, color=(255,0,0), x = -1, y = -1):
        self.minx = fminx
        self.maxx = fmaxx
        self.miny = fminy
        self.maxy = fmaxy-10
        self.w = width
        self.h = height
        self.env = env
        
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
        
        self.x = x if x > -1 else random.randint(fminx, fmaxx)
        self.y = y if y > -1 else random.randint(fminy, fmaxy)
        self.d = random.randint(1,4)

        self.old_d = self.d
        
    def getColor(self):
        return self.color
    
    def getCoords(self):
        return (self.x, self.y, self.w, self.h)
    
    def getCenter(self):
        return (self.x + (self.w / 2), self.y + (self.h / 2))
    
    def getHead(self):
        if self.d == 2:
            return (self.x + (self.w / 2), self.y)
        if self.d == 3:
            return (self.x + (self.w / 2), self.y + self.h)
        if self.d == 4:
            return (self.x, self.y + (self.h / 2))
        if self.d == 1:
            return (self.x + self.w, self.y + (self.h / 2))
    
    def randomMove(self):
        #print("Pos:",(self.x, self.y),"->",self.env.getCase(self.x, self.y))
        #print("dir:", ["up", "right", "down", "left"][self.d-1])
        #print("range:", self.w)
        print("color: ", self.getColor())
        print("perception:", self.env.getPerception(self.x, self.y, self.w, self.d))
        
        self.old_d = self.d
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

class EnvWorld:
    def __init__(self, fminx, fmaxx, fminy, fmaxy):
        self.map = [[(random.choice([2, 3, 4, 5, 6]) if random.randint(1, 1000) == 1 else 0) for _ in range(fmaxy - fminy)] for _ in range(fmaxx - fminx)]
        #remplir que avec des valeurs positives

        self.minx = fminx
        self.miny = fminy
        self.maxx = fmaxx
        self.maxy = fmaxy

        #self.expendValues()
        #self.expendValues()

        print("Init map")
        self.printMap()

    def getDims(self):
        return (len(self.map), len(self.map[0]))

    def expendValues(self):
        map2 = self.map.copy()
        for x in range(self.maxx - self.minx):
            for y in range(self.maxy - self.miny):
                if self.map[x][y] == 2:
                    neighbors = self.getCasesNeighbors(x, y)

                    for (x2, y2) in neighbors:
                        if self.isValidCoords(x2, y2):
                            try:
                                map2[x2][y2] = 2
                            except IndexError:
                                print("Index : ",x2, y2)
        self.map = map2.copy()

    def printMap(self):
        print("[")
        for l in self.map:
            print(l)
        print("]")

    def draw(self, win):
        for x in range(self.maxx - self.minx):
            for y in range(self.maxy - self.miny):
                if self.map[x][y] == 2:
                    pygame.draw.ellipse(win, (0, 255, 0), (self.minx+x, self.miny+y, 3, 3))
                if self.map[x][y] == 3:
                    pygame.draw.ellipse(win, (255, 0, 0), (self.minx+x, self.miny+y, 3, 3))
                if self.map[x][y] == 4:
                    pygame.draw.ellipse(win, (255, 140, 0), (self.minx+x, self.miny+y, 3, 3))
                if self.map[x][y] == 5:
                    pygame.draw.ellipse(win, (70, 130, 180), (self.minx+x, self.miny+y, 3, 3))
                if self.map[x][y] == 6:
                    pygame.draw.ellipse(win, (138, 43, 226), (self.minx+x, self.miny+y, 3, 3))

    def getCasesNeighbors(self, posx, posy):
        bloc = self.getFacesCases(posx, posy, 1, 1)
        bloc.extend(self.getFacesCases(posx, posy, 2, 1))
        bloc.extend(self.getFacesCases(posx, posy, 3, 1))
        bloc.extend(self.getFacesCases(posx, posy, 4, 1))

        return list(set(bloc))

    def getFacesCases(self, posx, posy, direction, nbSide):
        if direction == 1: #up
            bloc_a_gauche = [(posx-i, posy-1) for i in reversed(range(1, nbSide))]
            bloc_devant = [(posx, posy-1)]
            bloc_a_droite = [(posx+i, posy-1) for i in range(1, nbSide)]
        if direction == 2: #right
            bloc_a_gauche = [(posx+1, posy-i) for i in reversed(range(1, nbSide))]
            bloc_devant = [(posx+1, posy)]
            bloc_a_droite = [(posx+1, posy+i) for i in range(1, nbSide)]
        if direction == 3: #down
            bloc_a_gauche = [(posx+i, posy+1) for i in reversed(range(1, nbSide))]
            bloc_devant = [(posx, posy+1)]
            bloc_a_droite = [(posx-i, posy+1) for i in range(1, nbSide)] 
        if direction == 4: #left
            bloc_a_gauche = [(posx-1, posy+i) for i in reversed(range(1,nbSide))]
            bloc_devant = [(posx-1, posy)]
            bloc_a_droite = [(posx-1, posy-i) for i in range(1,nbSide)]

        bloc = bloc_a_gauche
        bloc.extend(bloc_devant)
        bloc.extend(bloc_a_droite)

        return list(bloc)

    def isValidCoords(self, posx, posy):
        return posx >= self.minx and posx <= self.maxx and posy >= self.miny and posy <= self.maxy

    def getPerception(self, posx, posy, rangexyEachSide, direction):
        #direction 1:up 2:right, 3:down, 4:left

        facesCases = self.getFacesCases(posx, posy, direction, rangexyEachSide)

        percep = []
        for case in facesCases:
            if self.isValidCoords(case[0], case[1]):
                percep.append(self.map[case[0]][case[1]])
            else:
                percep.append(-1)

        return percep

    def getCase(self, posx, posy):
        return self.map[posx][posy]
        
class Tick:
    def __init__(self, win):
        self.t = 0
        self.win = win
        self.myfont = pygame.font.SysFont("Arial", 16)
        
    def tick(self):
        s = "Tick :"+str(self.t)
        label = self.myfont.render(s, 1, (0, 0, 0))
        self.win.blit(label, (0, 0))
        
        self.t += 1
        s = "Tick :"+str(self.t)
        
        label = self.myfont.render(s, 1, (255, 255, 255))
        self.win.blit(label, (0, 0))

class Window:
    def __init__(self, width, height, caption= "My PyGame"):
        self.win = pygame.display.set_mode((width,height))
        pygame.display.set_caption(caption)
        
        self.width = width
        self.height = height
        
    def run(self, function):
        function(self.win,self.width, self.height)
        
def myrun(win, width, height):
    run = True
    env = EnvWorld(0, width, 0, height)
    ellipses = [Elipse(0, width, 0, height, 10, 10, env), 
                Elipse(0, width, 0, height, 10, 10, env, color=(255, 0, 255)), 
                Elipse(0, width, 0, height, 10, 10, env, color=(0, 255, 0))]
    
    t = Tick(win)
    env.draw(win)
    pygame.display.update()

    print("Run")
    while run:
        pygame.time.delay(50)
        
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

        env.draw(win)
        
        t.tick()
        
        pygame.display.update()
    pygame.quit()

myWin = Window(640, 480, "Test bestioles")
myWin.run(myrun)
