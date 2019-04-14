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
    
    def compare_fitness(self, entity1, entity2):
        if str(constantes.getTopLevelParentClassAfterObject(entity1)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity1 need to be an entity")
        if str(constantes.getTopLevelParentClassAfterObject(entity2)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity2 need to be an entity")
        pass