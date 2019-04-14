# -*- coding: utf-8 -*-

from . import constantes
from . import exceptions

class Statistique:
    def __init__(self, population):
        if str(constantes.getTopLevelParentClassAfterObject(population)) != "Population" :
            raise exceptions.NotAPopulation("", "population need to be an Population")
            
        self.targetPopulation = population
        
    def getInformations(self):
        return [self.targetPopulation.getEntitiesFitness(),  self.targetPopulation.getEntitiesDictionnaries()]