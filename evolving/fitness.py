# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Fitness:
    def __init__(self):
        pass
    
    def entity_fitness(self, entity):
        #need to think of name of entity class method
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
        pass
    
    def compare_fitness(self, fitness1, fitness2):
        #return -1 if 1<2, 0 if 1=2, 1 else
        pass