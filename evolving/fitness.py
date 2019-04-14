# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Fitness:
    def __init__(self):
        pass
    
    def entity_fitness(self, entity):
        if str(constantes.getTopLevelParentClassAfterObject(entity)) != "Entity" :
            raise exceptions.NotAnEntity("", "entity need to be an entity")
        pass
    
    def compare_fitness(self, entity1, entity2):
        pass