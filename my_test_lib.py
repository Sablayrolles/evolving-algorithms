# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 00:31:19 2019

@author: Megaport
"""

""" to do : 
    V 1) create for each specie you want a class of own fitness herited from Fitness class
    V 2) create a set of species herited from Specie class
    V 3) create a set of Entities class for each specie herited from Entity class
    4) create a population herited from Population class for your set of entities class and species
"""

import evolving

class NotANumberSpeed(Exception):
    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

#fitness 1)
class FitnessBlock(evolving.fitness.Fitness):
    def entity_fitness(self, entity):
        super().entity_fitness(entity)
        
        return entity.getPosX
    
    def compare_fitness(self, entity1, entity2):
        super().compare_fitness(entity1, entity2)
        
        if self.entity_fitness(entity1) < self.entity_fitness(entity2):
            return -1
        else:
            if self.entity_fitness(entity1) == self.entity_fitness(entity2):
                return 0
            else:
                return -1
f = FitnessBlock()

"""
---------------------
"""
     
#species 2)
class Blocs(evolving.specie.Specie):
    def __init__(self, fitness, name=""):
        super().__init__(fitness, name=name)
s = Blocs(f, "Blocs")

"""
---------------------
"""
   
#entity class 3)
class BlocEntity(evolving.entity.Entity):
    def __init__(self, specie, speed):
        super().__init__(specie, reproduction_max_child=1)
        
        if str(type(speed)) != "<class 'int'>" and str(type(speed)) != "<class 'float'>":
            print(str(type(speed)))
            raise NotANumberSpeed("", "speed need to be an int or a float")
            
        self.speed = speed
        
        self.posX = 0
        self.maxTime = 100
        
    def getPosX(self):
        return self.posX
    
    def move(self):
        self.posX += self.speed
        
    def isTimeToDie(self):
        return self.internclock > self.maxTime
    
    def _lifeCycle(self):
        super()._lifeCycle()
        
        self.move()
        
    def live(self):
        while not self.isTimeToDie():
            self._lifeCycle()
            
e = BlocEntity(s, 0.2)       
        
"""
---------------------
"""